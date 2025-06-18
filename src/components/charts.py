"""Chart creation components for the dashboard."""

from typing import List, Dict, Optional, Union
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from collections import defaultdict

from src.config import PRIMARY_COLOR, STYLE_VARS

# Font size configurations
TITLE_FONT_SIZE = STYLE_VARS["FONT_SIZE"] + 2  # Slightly larger for titles
LABEL_FONT_SIZE = STYLE_VARS["FONT_SIZE"]  # Base size for labels
ANNOTATION_FONT_SIZE = STYLE_VARS["FONT_SIZE"]  # Base size for annotations

def create_no_data_figure(title: Optional[str] = None) -> go.Figure:
    """Create a placeholder figure when no data is available."""
    fig = go.Figure()
    
    fig.add_annotation(
        text="No data available",
        x=0.5, y=0.5,
        xref="paper", yref="paper",
        showarrow=False,
        font=dict(size=ANNOTATION_FONT_SIZE, color="gray"),
    )
    
    fig.update_layout(
        title=title if title else None,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=30 if title else 10, b=10),
        height=300,
        font=dict(
            family=STYLE_VARS["FONT_FAMILY"],
            size=LABEL_FONT_SIZE
        )
    )
    
    return fig

def simplify_label(col: str) -> str:
    """Simplify column labels for better visualization.
    
    For multi-select questions, extracts only the option part after [...]
    For regular questions, returns the original text.
    """
    # Handle numeric values by converting to string
    if pd.isna(col):
        return "N/A"
    
    # Convert to string if numeric
    col = str(col)
    
    # First check if it's a multi-select question with square brackets
    if '[' in col and ']' in col:
        # Extract text between square brackets
        start = col.find('[') + 1
        end = col.rfind(']')  # Use rfind to handle nested brackets
        if end == -1:  # If no closing bracket found
            end = len(col)
        option = col[start:end].strip()
        
        # Clean up any trailing spaces or brackets
        option = option.strip(' ]')
        
        # If the option contains explanatory text in parentheses, keep it clean
        if '(' in option and ')' in option:
            parts = option.split('(', 1)
            explanation = parts[1].split(')')[0]
            return f"{parts[0].strip()} ({explanation})"
        
        return option
    
    # For regular questions, try to extract just the answer part
    # Common patterns in the questions
    patterns = [
        "What hinders you from incorporating sustainability in your role-specific tasks?",
        "Which sustainability dimension(s) do you feel you lack sufficient knowledge or tools to effectively address?",
        "What additional support or resources would help you integrate digital sustainability into your work?",
        "What drives you to incorporate sustainability in your role-related tasks?",
        "Do you incorporate",
        "Are there specific",
        "Does your organization",
        "How frequently",
        "Have you participated",
        "Are you satisfied"
    ]
    
    # Remove any known question patterns
    text = col
    for pattern in patterns:
        text = text.replace(pattern, "").strip()
    
    # Remove any remaining question marks and clean up
    text = text.split('?')[-1].strip()
    
    # Clean up any leading/trailing punctuation and whitespace
    text = text.strip('[]() .,:-')
    
    # If the text is empty after cleaning, return the original
    if not text:
        return col
    
    return text

def make_bar_chart(
    df: pd.DataFrame,
    col: str,
    title: Optional[str] = None,
    horizontal: bool = False
) -> go.Figure:
    """Create a bar chart for a categorical column."""
    if df[col].notna().sum() == 0:
        return create_no_data_figure(title)
    
    counts = df[col].value_counts(dropna=False).reset_index()
    counts.columns = [col, "count"]
    
    if counts.shape[0] == 0 or (counts.shape[0] == 1 and pd.isna(counts[col].iloc[0])):
        return create_no_data_figure(title)
    
    # Simplify the labels for display
    counts['display_label'] = counts[col].apply(simplify_label)
    
    if horizontal:
        counts = counts.sort_values("count")
        fig = px.bar(
            counts,
            y='display_label',  # Use simplified labels
            x="count",
            template="plotly_white",
            color_discrete_sequence=[PRIMARY_COLOR]
        )
        fig.update_traces(
            hoverinfo='none',  # Remove hover effect
            text=counts["count"],  # Show count as text
            textposition='outside',
            textfont=dict(size=LABEL_FONT_SIZE)
        )
        fig.update_layout(
            title=dict(
                text=title if title else None,
                font=dict(size=TITLE_FONT_SIZE)
            ),
            yaxis_title=None,
            xaxis_title="Count",
            height=350,
            margin=dict(l=10, r=10, t=30 if title else 10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                family=STYLE_VARS["FONT_FAMILY"],
                size=LABEL_FONT_SIZE
            )
        )
    else:
        fig = px.bar(
            counts,
            x='display_label',  # Use simplified labels
            y="count",
            template="plotly_white",
            color_discrete_sequence=[PRIMARY_COLOR]
        )
        fig.update_traces(
            hoverinfo='none',  # Remove hover effect
            text=counts["count"],  # Show count as text
            textposition='outside',
            textfont=dict(size=LABEL_FONT_SIZE)
        )
        fig.update_layout(
            title=dict(
                text=title if title else None,
                font=dict(size=TITLE_FONT_SIZE)
            ),
            xaxis_title=None,
            yaxis_title="Count",
            margin=dict(l=10, r=10, t=30 if title else 10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                family=STYLE_VARS["FONT_FAMILY"],
                size=LABEL_FONT_SIZE
            )
        )
    return fig

def make_pie_chart(df: pd.DataFrame, col: str, title: Optional[str] = None) -> go.Figure:
    """Create a pie chart for a categorical column."""
    if df[col].notna().sum() == 0:
        return create_no_data_figure(title)
    
    counts = df[col].value_counts(dropna=False).reset_index()
    counts.columns = [col, "count"]
    
    if counts.shape[0] == 0 or (counts.shape[0] == 1 and pd.isna(counts[col].iloc[0])):
        return create_no_data_figure(title)
    
    total = counts["count"].sum()
    counts["percentage"] = counts["count"] / total * 100
    
    fig = px.pie(
        counts,
        names=col,
        values="count",
        template="plotly_white",
        color_discrete_sequence=[PRIMARY_COLOR],
        hole=0.4
    )
    
    # Always show only percentages on slices and labels in legend
    fig.update_traces(
        textposition='inside',
        textinfo='percent',  # Only show percentage
        hoverinfo='none',  # Remove hover effect
        textfont=dict(size=LABEL_FONT_SIZE),
        showlegend=True  # Always show legend
    )
    
    fig.update_layout(
        title=dict(
            text=title if title else None,
            font=dict(size=TITLE_FONT_SIZE)
        ),
        margin=dict(l=10, r=120, t=30 if title else 10, b=10),
        legend=dict(
            yanchor="middle",
            y=0.5,
            xanchor="right",
            x=1.2,
            font=dict(size=LABEL_FONT_SIZE)
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family=STYLE_VARS["FONT_FAMILY"],
            size=LABEL_FONT_SIZE
        ),
        height=500
    )
    
    fig.add_annotation(
        text=f"Total<br>{total}",
        x=0.5, y=0.5,
        font=dict(size=ANNOTATION_FONT_SIZE),
        showarrow=False
    )
    return fig

def make_donut_chart(df: pd.DataFrame, col: str, title: Optional[str] = None) -> go.Figure:
    """Create a donut chart for a categorical column."""
    if df[col].notna().sum() == 0:
        return create_no_data_figure(title)
    
    counts = df[col].value_counts(dropna=False)
    
    fig = px.pie(
        names=counts.index.astype(str),
        values=counts.values,
        hole=0.5,
        title=title,
        color_discrete_sequence=[PRIMARY_COLOR]
    )
    
    # Always show only percentages on slices and labels in legend
    fig.update_traces(
        textposition='inside',
        textinfo='percent',  # Only show percentage
        hoverinfo='none',  # Remove hover effect
        textfont=dict(size=LABEL_FONT_SIZE),
        showlegend=True  # Always show legend
    )
    
    fig.update_layout(
        title=dict(
            text=title if title else None,
            font=dict(size=TITLE_FONT_SIZE)
        ),
        margin=dict(l=10, r=120, t=30 if title else 10, b=10),
        legend=dict(
            yanchor="middle",
            y=0.5,
            xanchor="right",
            x=1.2,
            font=dict(size=LABEL_FONT_SIZE)
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family=STYLE_VARS["FONT_FAMILY"],
            size=LABEL_FONT_SIZE
        ),
        height=500,
        hovermode=False
    )
    
    # Add total in the center
    total = counts.sum()
    fig.add_annotation(
        text=f"Total<br>{total}",
        x=0.5, y=0.5,
        font=dict(size=ANNOTATION_FONT_SIZE),
        showarrow=False
    )
    
    return fig

def make_histogram(
    df: pd.DataFrame,
    col: str,
    title: Optional[str] = None,
    bins: int = 10,
    kde: bool = True
) -> go.Figure:
    """Create a histogram for a numeric column with option for KDE curve."""
    numeric_values = pd.to_numeric(df[col], errors='coerce')
    valid_data_count = numeric_values.notna().sum()
    
    if valid_data_count < 3:
        return create_no_data_figure(title)
    
    if kde:
        hist_data = numeric_values.dropna()
        fig = go.Figure()
        
        fig.add_trace(go.Histogram(
            x=hist_data,
            nbinsx=bins,
            marker_color=PRIMARY_COLOR,
            opacity=0.7,
            name="Count",
            hoverinfo='none',  # Remove hover effect
            showlegend=False
        ))
        
        fig.update_layout(
            title=dict(
                text=title if title else None,
                font=dict(size=TITLE_FONT_SIZE)
            ),
            xaxis_title=None,
            yaxis_title="Frequency",
            template="plotly_white",
            margin=dict(l=10, r=10, t=30 if title else 10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                family=STYLE_VARS["FONT_FAMILY"],
                size=LABEL_FONT_SIZE
            )
        )
    else:
        fig = px.histogram(
            df,
            x=numeric_values,
            nbins=bins,
            template="plotly_white",
            color_discrete_sequence=[PRIMARY_COLOR]
        )
        fig.update_traces(
            hoverinfo='none'  # Remove hover effect
        )
        fig.update_layout(
            title=dict(
                text=title if title else None,
                font=dict(size=TITLE_FONT_SIZE)
            ),
            xaxis_title=None,
            yaxis_title="Frequency",
            margin=dict(l=10, r=10, t=30 if title else 10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                family=STYLE_VARS["FONT_FAMILY"],
                size=LABEL_FONT_SIZE
            )
        )
    return fig

def make_world_map(df: pd.DataFrame, col: str, title: Optional[str] = None) -> go.Figure:
    """Create a choropleth map for countries or continents."""
    if df[col].notna().sum() == 0:
        return create_no_data_figure(title)
    
    counts = df[col].value_counts(dropna=False)
    
    fig = px.choropleth(
        locations=counts.index,
        locationmode="country names",
        color=counts.values,
        hover_name=counts.index,
        color_continuous_scale=px.colors.sequential.Plasma,
        title=title
    )
    
    fig.update_layout(
        title=dict(
            text=title if title else None,
            font=dict(size=TITLE_FONT_SIZE)
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family=STYLE_VARS["FONT_FAMILY"],
            size=LABEL_FONT_SIZE
        ),
        margin=dict(l=10, r=10, t=30 if title else 10, b=10),
        hovermode=False
    )
    
    return fig

def make_multi_select_bar(df: pd.DataFrame, cols: List[str], title: Optional[str] = None) -> go.Figure:
    """Create a horizontal bar chart for multiple-select questions."""
    if not cols or df.empty:
        return create_no_data_figure(title)
    
    # Count responses for each option
    counts = []
    for col in cols:
        if col in df:
            count = df[col].fillna(0).astype(bool).sum()
            total = len(df)
            if total > 0:
                percentage = (count / total) * 100
                # Extract text within brackets if present, otherwise use full text
                label = col
                if '[' in col and ']' in col:
                    start = col.find('[') + 1
                    end = col.rfind(']')
                    label = col[start:end].strip()
                counts.append({
                    'option': label,
                    'count': count,
                    'percentage': percentage
                })
    
    if not counts:
        return create_no_data_figure(title)
    
    # Sort by count in descending order
    counts_df = pd.DataFrame(counts).sort_values('count', ascending=True)
    
    # Create the horizontal bar chart
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=counts_df['count'],
        y=counts_df['option'],
        orientation='h',
        marker_color=PRIMARY_COLOR,
        text=[f"{count} ({percentage:.1f}%)" for count, percentage in zip(counts_df['count'], counts_df['percentage'])],
        textposition='outside',
        hoverinfo='none',  # Remove hover effect
        textfont=dict(size=LABEL_FONT_SIZE)
    ))
    
    # Update layout
    fig.update_layout(
        title=dict(
            text=title if title else None,
            font=dict(size=TITLE_FONT_SIZE)
        ),
        xaxis_title="Number of Responses",
        yaxis_title=None,
        template="plotly_white",
        margin=dict(l=10, r=10, t=30 if title else 10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family=STYLE_VARS["FONT_FAMILY"],
            size=LABEL_FONT_SIZE
        ),
        showlegend=False,
        height=max(300, len(counts) * 40)  # Adjust height based on number of options
    )
    
    # Update axes
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
    fig.update_yaxes(showgrid=False)
    
    return fig

def generate_grouped_bar_chart(df: pd.DataFrame, cols: List[str], title: Optional[str] = None) -> go.Figure:
    """
    Create a bar chart for grouped multi-column questions (e.g., regions, barriers).
    Each bar is the count of 'Yes' responses for that option/column.
    """
    if not cols or df.empty:
        return create_no_data_figure(None)
    counts = []
    for col in cols:
        if col in df:
            count = (df[col].fillna('').astype(str).str.strip().str.lower() == 'yes').sum()
            # Extract label from column name
            label = simplify_label(col)
            counts.append({'option': label, 'count': count})
    if not counts:
        return create_no_data_figure(None)
    counts_df = pd.DataFrame(counts).sort_values('count', ascending=False)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=counts_df['option'],
        y=counts_df['count'],
        marker_color=PRIMARY_COLOR,
        text=counts_df['count'],
        textposition='outside',
        hoverinfo='none',
        textfont=dict(size=LABEL_FONT_SIZE)
    ))
    fig.update_layout(
        xaxis_title=None,
        yaxis_title="Count",
        template="plotly_white",
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family=STYLE_VARS["FONT_FAMILY"],
            size=LABEL_FONT_SIZE
        ),
        showlegend=False,
        height=max(300, len(counts) * 40)
    )
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
    fig.update_yaxes(showgrid=False)
    return fig

def generate_chart(
    df: pd.DataFrame,
    col: str,
    title: Optional[str] = None,
    chart_type: str = 'auto'
) -> go.Figure:
    """Automatically generate an appropriate chart based on data type."""
    df_copy = df.copy()

    if df_copy[col].count() == 0:
        return create_no_data_figure(title)

    if chart_type == 'auto':
        if pd.api.types.is_numeric_dtype(df_copy[col]):
            return make_histogram(df_copy, col, title, kde=True)
        elif "continent" in col.lower() or "country" in col.lower():
            try:
                return make_world_map(df_copy, col, title)
            except Exception as e:
                print(f"Error creating map for {col}: {str(e)}")
                return make_bar_chart(df_copy, col, title, horizontal=True)
        else:
            unique_count = df_copy[col].nunique()
            if unique_count <= 5:
                return make_donut_chart(df_copy, col, title)
            else:
                return make_bar_chart(df_copy, col, title, horizontal=True)
    elif chart_type == 'bar':
        return make_bar_chart(df_copy, col, title)
    elif chart_type == 'bar_h':
        return make_bar_chart(df_copy, col, title, horizontal=True)
    elif chart_type == 'histogram':
        if pd.api.types.is_numeric_dtype(df_copy[col]):
            return make_histogram(df_copy, col, title)
        else:
            print(f"Warning: Tried to make histogram of non-numeric column {col}")
            return make_bar_chart(df_copy, col, title)
    elif chart_type == 'pie':
        return make_pie_chart(df_copy, col, title)
    elif chart_type == 'donut':
        return make_donut_chart(df_copy, col, title)
    elif chart_type == 'map':
        return make_world_map(df_copy, col, title)
    else:
        return make_bar_chart(df_copy, col, title) 