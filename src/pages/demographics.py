"""Demographics page module."""

import pandas as pd
import dash_bootstrap_components as dbc
from dash import html
from src.config import DEMOGRAPHIC_COLS, APPLICATION_DOMAIN_COLS, GROUPED_QUESTIONS
from src.components.charts import generate_chart, generate_grouped_bar_chart
from src.components.layout import build_chart_card, build_chart_grid

def build_demographics_page(df: pd.DataFrame) -> html.Div:
    # Debug: Print unique values for the '[Other]' ChatGPT usage column
    other_col = "How often do you use ChatGPT or similar AI chatbots? [Other]"
    if other_col in df.columns:
        print(f"[DEBUG] Unique values for '{other_col}': {df[other_col].unique()}")
    # Single-value demographic questions (not grouped)
    single_cols = [col for col in DEMOGRAPHIC_COLS if not any(col in group['columns'] for group in GROUPED_QUESTIONS.values())]
    chart_info = []
    for col in single_cols:
        # Robustly skip '[Other]' charts if all values are missing or empty, or if the main question is not present
        if col not in df.columns:
            continue
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
        fig = generate_chart(df, col, chart_type='bar')
        chart_info.append((col, fig))
    # Grouped questions: regions, roles, application domains
    grouped_cards = []
    for key in ["regions", "roles", "application_domains"]:
        group = GROUPED_QUESTIONS[key]
        fig = generate_grouped_bar_chart(df, group['columns'], group['question'])
        card = build_chart_card(group['question'], fig)
        grouped_cards.append(card)
    return html.Div([
        html.H3("Demographics", className="mb-4 mt-2"),
        *build_chart_grid(chart_info, cards_per_row=2),
        dbc.Row([dbc.Col(card, width=6) for card in grouped_cards], className="mb-4 g-4"),
    ]) 