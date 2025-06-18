import dash_bootstrap_components as dbc
from dash import html
from src.config import GROUPED_QUESTIONS
from src.components.charts import generate_grouped_bar_chart
from src.components.layout import build_chart_card

def build_barriers_page(df):
    """Build the Barriers page layout for GenAI RE survey."""
    group = GROUPED_QUESTIONS["barriers"]
    fig = generate_grouped_bar_chart(df, group['columns'], group['question'])
    card = build_chart_card(group['question'], fig)
    return html.Div([
        html.H3("Barriers to GenAI in RE", className="mb-4 mt-2"),
        dbc.Row(dbc.Col(card, width=12), className="mb-4"),
    ]) 