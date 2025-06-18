from dash import html
from src.config.config import GROUPED_QUESTIONS
from src.components.charts import generate_grouped_bar_chart
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

def build_barriers_page(df):
    """Build the Barriers page layout for GenAI RE survey."""
    group = GROUPED_QUESTIONS["barriers"]
    fig = generate_grouped_bar_chart(df, group['columns'], None)  # horizontal by default
    return html.Div([
        html.H3("Barriers to GenAI in RE", className="mb-4 mt-2", style=SECTION_HEADER_STYLE),
        html.H5(group['question'], className="mb-3", style={"color": PRIMARY_COLOR, "fontWeight": 600, "fontSize": "1.25rem"}),
        build_chart_card("", fig, 12),
    ]) 