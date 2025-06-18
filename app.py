"""Main application file for the GenAI in RE Survey Dashboard."""

import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output

from src.config import CONTENT_STYLE, YEAR_TO_FILE, AVAILABLE_YEARS
from src.components.layout import create_sidebar
from src.utils.data_processing import load_data_file
from src.pages.demographics import build_demographics_page
from src.pages.experience import build_experience_page
from src.pages.genai_usage import build_genai_usage_page
from src.pages.barriers import build_barriers_page
from src.pages.insights import build_insights_page
# (Add more imports for new sections as needed)

# Initialize the Dash app
external_stylesheets = [dbc.themes.YETI, dbc.icons.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
app.title = "GenAI in RE Survey Dashboard"

# Create the app layout
app.layout = dbc.Container([
    dcc.Location(id="url", refresh=False),
    dcc.Dropdown(id="year-dropdown", style={"display": "none"}),  # Hidden placeholder for callback registration
    html.Div(id="sidebar-container"),
    html.Div(id="page-content", style=CONTENT_STYLE),
], fluid=True, style={"min-height": "100vh", "background-color": "#f8f9fa"})

# Callback to update sidebar and page content based on URL and year
@app.callback(
    [Output("sidebar-container", "children"), Output("page-content", "children")],
    [Input("url", "pathname"), Input("year-dropdown", "value")]
)
def render_page_and_sidebar(pathname: str, selected_year: int):
    """
    Render the sidebar and appropriate page content based on the URL pathname and selected year.
    """
    # Default to latest year if not set
    if not selected_year:
        selected_year = max(AVAILABLE_YEARS)
    # Load data for the selected year
    data_file = YEAR_TO_FILE.get(selected_year)
    df = load_data_file(data_file)
    # Sidebar with year selection
    sidebar = create_sidebar(selected_year=selected_year)
    # Route to the appropriate page
    if pathname == "/":
        content = dbc.Container([build_demographics_page(df)], fluid=True)
    elif pathname == "/experience":
        content = dbc.Container([build_experience_page(df)], fluid=True)
    elif pathname == "/genai-usage":
        content = dbc.Container([build_genai_usage_page(df)], fluid=True)
    elif pathname == "/barriers":
        content = dbc.Container([build_barriers_page(df)], fluid=True)
    elif pathname == "/insights":
        content = dbc.Container([build_insights_page(df)], fluid=True)
    else:
        content = dbc.Container(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
                dbc.Button("Go to Homepage", href="/", color="primary", className="mt-3")
            ],
            className="py-5 text-center",
        )
    return sidebar, content

if __name__ == "__main__":
    app.run(debug=True, port=8053)
