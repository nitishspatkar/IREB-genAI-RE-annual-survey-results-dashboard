import dash_bootstrap_components as dbc
from dash import html
from src.config import RE_EXPERIENCE_COLS
from src.components.charts import generate_chart
from src.components.layout import build_chart_card, build_chart_grid

def build_experience_page(df):
    """Build the RE experience page layout for GenAI RE survey."""
    chart_info = [(col, generate_chart(df, col, chart_type='bar')) for col in RE_EXPERIENCE_COLS if col in df.columns]
    return html.Div([
        html.H3("RE Experience & Skills", className="mb-4 mt-2"),
        *build_chart_grid(chart_info, cards_per_row=2),
    ]) 