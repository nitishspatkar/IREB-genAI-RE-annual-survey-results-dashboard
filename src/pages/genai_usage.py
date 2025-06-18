import dash_bootstrap_components as dbc
from dash import html
from src.config.config import GENAI_USAGE_COLS, GENAI_RE_DISCIPLINE_COLS, GROUPED_QUESTIONS
from src.components.charts import generate_chart, generate_grouped_bar_chart
from src.components.layout import build_chart_card, build_chart_grid

PRIMARY_COLOR = "#831E82"
SECTION_HEADER_STYLE = {
    "color": PRIMARY_COLOR,
    "marginTop": "2.5rem",
    "marginBottom": "1.2rem",
    "fontSize": "1.35rem",
    "fontWeight": 700,
    "borderBottom": f"2px solid {PRIMARY_COLOR}",
    "paddingBottom": "0.3rem"
}
CARD_ROW_STYLE = "mb-4 g-4"
COMMENT_HEADER_STYLE = {
    "color": PRIMARY_COLOR,
    "fontWeight": 700,
    "fontSize": "1.25rem",
    "marginBottom": "0.9rem",
    "marginTop": "1.5rem",
    "letterSpacing": "-0.5px"
}
COMMENT_LIST_STYLE = {
    "fontSize": "1.13rem",
    "color": "#222",
    "paddingLeft": "1.2rem",
    "marginBottom": 0,
    "maxHeight": "350px",
    "overflowY": "auto"
}
CARD_STYLE = {
    "boxShadow": "0 2px 8px rgba(131,30,130,0.08)",
    "border": f"1px solid {PRIMARY_COLOR}",
    "borderRadius": "0.5rem",
    "background": "#fff",
    "marginBottom": "2.5rem",
    "padding": "1.2rem 1.5rem 1.2rem 1.5rem"
}

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
        question_text = col.strip()
        if question_text.endswith('?'):
            question_text = question_text[:-1]
        fig = generate_chart(df, col, chart_type='bar_h')
        usage_info.append(html.Div([
            html.H5(question_text, className="mb-3", style={"color": PRIMARY_COLOR, "fontWeight": 700, "fontSize": "1.25rem"}),
            build_chart_card("", fig, 12)
        ]))
    # Grouped chart for RE disciplines
    group = GROUPED_QUESTIONS["genai_re_disciplines"]
    discipline_fig = generate_grouped_bar_chart(df, group['columns'], None)
    discipline_card = html.Div([
        html.H5("For which RE disciplines did you use GenAI?", className="mb-3", style={"color": PRIMARY_COLOR, "fontWeight": 700, "fontSize": "1.25rem"}),
        build_chart_card("", discipline_fig, 12)
    ])
    # Comments section
    comment_cols = [col for col in GENAI_RE_DISCIPLINE_COLS if col.endswith('[Comment]') or col.endswith('[Other comment]')]
    comments = []
    for col in comment_cols:
        if col in df.columns:
            non_empty = df[col].dropna().unique()
            if len(non_empty) > 0:
                comments.append(html.Div([
                    html.H4(col, style=COMMENT_HEADER_STYLE),
                    html.Ul([html.Li(str(val), style={"marginBottom": "0.7rem", "lineHeight": "1.6"}) for val in non_empty if str(val).strip()], style=COMMENT_LIST_STYLE)
                ], style=CARD_STYLE))
    return html.Div([
        html.H3("GenAI Usage in RE", className="mb-4 mt-2", style=SECTION_HEADER_STYLE),
        *usage_info,
        html.Hr(),
        discipline_card,
        html.Hr(),
        html.H3("Comments on GenAI Usage", className="mb-4", style=SECTION_HEADER_STYLE),
        *comments
    ]) 