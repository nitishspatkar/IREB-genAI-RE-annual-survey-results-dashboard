import dash_bootstrap_components as dbc
from dash import html
from src.config import GENAI_USAGE_COLS, GENAI_RE_DISCIPLINE_COLS, GROUPED_QUESTIONS
from src.components.charts import generate_chart, generate_grouped_bar_chart
from src.components.layout import build_chart_card, build_chart_grid

def build_genai_usage_page(df):
    """Build the GenAI usage page layout for GenAI RE survey."""
    usage_info = []
    for col in GENAI_USAGE_COLS:
        if col not in df.columns:
            continue
        if col.endswith('[Other]'):
            main_col = col.replace(' [Other]', '')
            if main_col not in GENAI_USAGE_COLS or main_col not in df.columns:
                continue
            series = df[col]
            if series.isna().all():
                continue
            non_empty = series.dropna().astype(str).str.strip()
            if (non_empty == '').all():
                continue
        fig = generate_chart(df, col, chart_type='bar')
        usage_info.append((col, fig))
    # Grouped chart for RE disciplines
    group = GROUPED_QUESTIONS["genai_re_disciplines"]
    discipline_fig = generate_grouped_bar_chart(df, group['columns'], group['question'])
    discipline_card = build_chart_card(group['question'], discipline_fig)
    comment_cols = [col for col in GENAI_RE_DISCIPLINE_COLS if col.endswith('[Comment]') or col.endswith('[Other comment]')]
    comments = []
    for col in comment_cols:
        if col in df.columns:
            non_empty = df[col].dropna().unique()
            if len(non_empty) > 0:
                comments.append(html.Div([
                    html.H5(col, className="mt-3 mb-2"),
                    html.Ul([html.Li(str(val)) for val in non_empty if str(val).strip()])
                ]))
    return html.Div([
        html.H3("GenAI Usage in RE", className="mb-4 mt-2"),
        *build_chart_grid(usage_info, cards_per_row=2),
        html.Hr(),
        discipline_card,
        html.Hr(),
        html.H4("Comments on GenAI Usage", className="mb-3"),
        *comments
    ]) 