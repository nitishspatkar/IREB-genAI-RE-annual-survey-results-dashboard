import dash_bootstrap_components as dbc
from dash import html
from src.config.open_ended import OPEN_ENDED_COLS

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

RESPONSE_LIST_STYLE = {
    "paddingLeft": "1.2rem",
    "marginBottom": 0,
    "maxHeight": "350px",
    "overflowY": "auto",
    "fontSize": "1.18rem",
    "color": "#222"
}

QUESTION_HEADER_STYLE = {
    "color": PRIMARY_COLOR,
    "fontWeight": 700,
    "fontSize": "1.25rem",
    "marginBottom": "0.9rem",
    "marginTop": "1.5rem",
    "letterSpacing": "-0.5px"
}

CARD_STYLE = {
    "boxShadow": "0 2px 8px rgba(131,30,130,0.08)",
    "border": f"1px solid {PRIMARY_COLOR}",
    "borderRadius": "0.5rem",
    "background": "#fff",
    "marginBottom": "2.5rem",
    "padding": "1.2rem 1.5rem 1.2rem 1.5rem"
}

def build_open_ended_page(df):
    sections = []
    for col in OPEN_ENDED_COLS + [c for c in df.columns if ('[Comment]' in c or '[Other comment]' in c) and c not in OPEN_ENDED_COLS]:
        if col in df.columns:
            responses = [r for r in df[col].dropna().astype(str).tolist() if r.strip() and r.strip().lower() != 'n/a']
            if responses:
                question_text = col.replace('[Comment]', '').replace('[Other comment]', '').replace('[Other]', '').strip()
                if question_text.endswith('?'):
                    question_text = question_text[:-1]
                sections.append(
                    html.Div([
                        html.H4(question_text, style=QUESTION_HEADER_STYLE),
                        html.Ul([
                            html.Li(r, style={"marginBottom": "0.7rem", "fontSize": "1.13rem", "lineHeight": "1.6"}) for r in responses
                        ], style=RESPONSE_LIST_STYLE)
                    ], style=CARD_STYLE)
                )
    return html.Div([
        html.H3("Open-Ended Responses & Comments", className="mb-4 pt-3", style=SECTION_HEADER_STYLE),
        html.P("This page summarizes all open-ended survey responses as a styled list for each question.", className="lead mb-5", style={"color": "#666", "fontSize": "1.1rem"}),
        *sections
    ]) 