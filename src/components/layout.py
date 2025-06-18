"""Layout components for the dashboard."""

from typing import List, Dict, Tuple, Union
import dash_bootstrap_components as dbc
from dash import html, dcc

from src.config import (
    STYLE_VARS,
    PRIMARY_COLOR,
    SIDEBAR_STYLE,
    AVAILABLE_YEARS
)

def clean_title(title: str) -> str:
    """Clean and standardize title text for consistent display."""
    # Remove emojis and special characters but keep basic punctuation
    cleaned = title.replace('🎯', '').replace('❓', '').strip()
    return cleaned

def build_stat_card(
    title: str,
    value: str,
    icon_class: str = "bi-info-circle",
    trend: Union[float, None] = None,
    subtitle: Union[str, None] = None
) -> dbc.Card:
    """Create a card with a key statistic and optional trend and subtitle."""
    card_content = [
        dbc.CardHeader([
            html.I(className=f"bi {icon_class} me-2"),
            html.Span(clean_title(title))
        ], className="d-flex align-items-center"),
        dbc.CardBody([
            html.H2(value, className="card-title text-center mb-0"),
            html.P(subtitle, className="card-text text-center text-muted small mt-2") if subtitle else None,
            html.Div([
                html.I(className=f"bi {'bi-arrow-up-short text-success' if trend and trend > 0 else 'bi-arrow-down-short text-danger'} me-1") if trend else None,
                html.Span(f"{abs(trend)}%", className=f"{'text-success' if trend and trend > 0 else 'text-danger'}") if trend else None
            ], className="text-center mt-2") if trend else None
        ])
    ]
    return dbc.Card(card_content, className="shadow-sm h-100 border-0")

def build_chart_card(
    title: str,
    fig: object,
    column_width: int = 12,
    className: str = "mb-4"
) -> dbc.Col:
    """Wraps a plotly figure in a Bootstrap card with custom styling."""
    return dbc.Col(
        dbc.Card([
            dbc.CardHeader(
                html.H5(clean_title(title), className="card-title mb-0"),
                className="card-header-primary border-bottom-0",
                style={"font-size": "1rem", "font-weight": "500"}
            ),
            dbc.CardBody(
                dcc.Graph(
                    figure=fig,
                    config={
                        'displayModeBar': False,
                        'staticPlot': True  # This disables all interactivity including hover
                    }
                ),
                className="pt-0"  # Remove top padding since header has no border
            )
        ], className="shadow-sm h-100 border-0"),
        width=column_width,
        className=className
    )

def build_card(col: str, fig: object, reverse_mapping: Dict[str, str]) -> dbc.Card:
    """
    Wraps an individual graph in a Bootstrap card.
    Uses the full question text (from reverse_mapping) for the header.
    """
    question_text = reverse_mapping.get(col, col.replace("_", " ").title())
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H5(clean_title(question_text), className="card-title mb-0"),
                className="card-header-primary border-bottom-0",
                style={"font-size": "1rem", "font-weight": "500"}
            ),
            dbc.CardBody(
                dcc.Graph(
                    figure=fig,
                    config={
                        'displayModeBar': False,
                        'staticPlot': True  # This disables all interactivity including hover
                    }
                ),
                className="pt-0"  # Remove top padding since header has no border
            )
        ],
        className="mb-4 shadow-sm border-0"
    )

def build_multi_card(title: str, fig: object) -> dbc.Card:
    """Wraps a multi-select visualization in a Bootstrap card."""
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H5(clean_title(title), className="card-title mb-0"),
                className="card-header-primary border-bottom-0",
                style={"font-size": "1rem", "font-weight": "500"}
            ),
            dbc.CardBody(
                dcc.Graph(
                    figure=fig,
                    config={
                        'displayModeBar': False,
                        'staticPlot': True  # This disables all interactivity including hover
                    }
                ),
                className="pt-0"  # Remove top padding since header has no border
            )
        ],
        className="mb-4 shadow-sm border-0"
    )

def build_section_three_columns(
    fig_pairs: List[Tuple[str, object]],
    reverse_mapping: Dict[str, str]
) -> dbc.Row:
    """
    Given a list of (column, figure) pairs, splits them into three columns
    and returns a Bootstrap Row with three Columns containing cards.
    """
    third = (len(fig_pairs) + 2) // 3  # Round up the split
    left_pairs = fig_pairs[:third]
    middle_pairs = fig_pairs[third:2*third]
    right_pairs = fig_pairs[2*third:]
    
    left_cards = [build_card(col, fig, reverse_mapping) for col, fig in left_pairs]
    middle_cards = [build_card(col, fig, reverse_mapping) for col, fig in middle_pairs]
    right_cards = [build_card(col, fig, reverse_mapping) for col, fig in right_pairs]
    
    return dbc.Row([
        dbc.Col(left_cards, width=4),
        dbc.Col(middle_cards, width=4),
        dbc.Col(right_cards, width=4)
    ], className="mb-4")

def build_chart_grid(
    chart_info_list: List[Tuple[str, object]],
    cards_per_row: int = 2
) -> List[dbc.Row]:
    """
    Given a list of (title, figure) pairs, returns a list of dbc.Row objects,
    each containing up to cards_per_row chart cards.
    """
    rows = []
    for i in range(0, len(chart_info_list), cards_per_row):
        row_cards = [
            build_chart_card(title, fig, 12 // cards_per_row)
            for title, fig in chart_info_list[i:i+cards_per_row]
        ]
        rows.append(dbc.Row(row_cards, className="mb-5 g-4"))
    return rows

def create_sidebar(selected_year=None):
    """Create the sidebar with navigation for GenAI RE survey sections and year selection."""
    return html.Div([
        html.H2("GenAI in RE Survey", className="display-7 mb-4"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(year), 'value': year} for year in AVAILABLE_YEARS],
            value=selected_year or AVAILABLE_YEARS[0],
            clearable=False,
            style={'margin-bottom': '1rem'}
        ),
        html.Hr(),
        dbc.Nav([
            dbc.NavLink([
                html.I(className="bi bi-people-fill me-2"),
                "Demographics"
            ], href="/", active="exact"),
            dbc.NavLink([
                html.I(className="bi bi-bar-chart-fill me-2"),
                "Experience"
            ], href="/experience", active="exact"),
            dbc.NavLink([
                html.I(className="bi bi-cpu me-2"),
                "GenAI Usage"
            ], href="/genai-usage", active="exact"),
            dbc.NavLink([
                html.I(className="bi bi-exclamation-triangle-fill me-2"),
                "Barriers"
            ], href="/barriers", active="exact"),
            dbc.NavLink([
                html.I(className="bi bi-lightbulb me-2"),
                "Insights"
            ], href="/insights", active="exact"),
        ], vertical=True, pills=True),
    ], style=SIDEBAR_STYLE) 