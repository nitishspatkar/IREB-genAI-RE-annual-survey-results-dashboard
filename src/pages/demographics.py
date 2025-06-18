"""Demographics page module."""

import pandas as pd
from dash import html
from src.config.config import DEMOGRAPHIC_COLS, GROUPED_QUESTIONS
from src.components.charts import generate_chart, generate_grouped_bar_chart
from src.components.layout import build_chart_card

PRIMARY_COLOR = "#831E82"
SECTION_HEADER_STYLE = {
    "color": PRIMARY_COLOR,
    "marginTop": "2.5rem",
    "marginBottom": "1.2rem",
    "fontSize": "1.2rem",
    "fontWeight": 600,
    "borderBottom": f"2px solid {PRIMARY_COLOR}",
    "paddingBottom": "0.3rem"
}
CARD_ROW_STYLE = "mb-4 g-4"

def build_demographics_page(df: pd.DataFrame) -> html.Div:
    """Build the demographics page layout for GenAI RE survey."""
    region_cols = set(GROUPED_QUESTIONS["regions"]["columns"])
    chart_info = []
    for col in DEMOGRAPHIC_COLS:
        if col not in df.columns:
            continue
        if col in region_cols:
            continue  # Skip region columns here, only show grouped chart below
        if col.endswith('[Other]'):
            main_col = col.replace(' [Other]', '')
            if main_col not in DEMOGRAPHIC_COLS or main_col not in df.columns:
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
        chart_info.append(html.Div([
            html.H5(question_text, className="mb-3", style={"color": PRIMARY_COLOR, "fontWeight": 600, "fontSize": "1.25rem"}),
            build_chart_card("", fig, 12)
        ]))

    # Grouped questions: regions, roles, application domains
    grouped_cards = []
    # Regions as a single grouped chart with a large header
    region_group = GROUPED_QUESTIONS["regions"]
    region_fig = generate_grouped_bar_chart(df, region_group['columns'], None)
    grouped_cards.append(html.Div([
        html.H5(region_group['question'], className="mb-3", style={"color": PRIMARY_COLOR, "fontWeight": 600, "fontSize": "1.25rem"}),
        build_chart_card("", region_fig, 12)
    ]))
    # Roles and application domains
    for key, label in zip(["roles", "application_domains"], ["Roles", "Application Domains"]):
        group = GROUPED_QUESTIONS[key]
        fig = generate_grouped_bar_chart(df, group['columns'], None)
        grouped_cards.append(html.Div([
            html.H5(label, className="mb-3", style={"color": PRIMARY_COLOR, "fontWeight": 600, "fontSize": "1.25rem"}),
            build_chart_card("", fig, 12)
        ]))

    return html.Div([
        html.H3("Demographics", className="mb-4 mt-2", style=SECTION_HEADER_STYLE),
        *chart_info,
        html.H4("Regions, Roles, and Application Domains", className="mb-3", style=SECTION_HEADER_STYLE),
        *grouped_cards,
    ]) 