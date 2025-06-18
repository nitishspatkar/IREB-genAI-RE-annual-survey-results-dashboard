"""Chart creation components for the dashboard."""

from typing import List, Dict, Optional, Union
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from collections import defaultdict
from wordcloud import WordCloud, STOPWORDS
import collections
import re
import unicodedata

from src.config.config import PRIMARY_COLOR, STYLE_VARS

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
    
    # Determine if we need to rotate x-axis labels
    rotate = False
    if not horizontal:
        if len(counts['display_label']) > 6 or any(len(str(lbl)) > 20 for lbl in counts['display_label']):
            rotate = True
    
    if horizontal:
        counts = counts.sort_values("count")
        fig = px.bar(
            counts,
            y='display_label',
            x="count",
            template="plotly_white",
            color_discrete_sequence=[PRIMARY_COLOR]
        )
        fig.update_traces(
            hoverinfo='none',
            text=counts["count"],
            textposition='outside',
            textfont=dict(size=LABEL_FONT_SIZE)
        )
        fig.update_layout(
            title=None,
            yaxis_title=None,
            xaxis_title="Count",
            height=350,
            margin=dict(l=10, r=10, t=30, b=40),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                family=STYLE_VARS["FONT_FAMILY"],
                size=LABEL_FONT_SIZE
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5
            )
        )
    else:
        fig = px.bar(
            counts,
            x='display_label',
            y="count",
            template="plotly_white",
            color_discrete_sequence=[PRIMARY_COLOR]
        )
        fig.update_traces(
            hoverinfo='none',
            text=counts["count"],
            textposition='outside',
            textfont=dict(size=LABEL_FONT_SIZE)
        )
        fig.update_layout(
            title=None,
            xaxis_title=None,
            yaxis_title="Count",
            margin=dict(l=10, r=10, t=30, b=80),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                family=STYLE_VARS["FONT_FAMILY"],
                size=LABEL_FONT_SIZE
            ),
            xaxis=dict(tickangle=-35 if rotate else 0)
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

def make_multi_select_bar(df: pd.DataFrame, cols: list, title: str = None) -> go.Figure:
    """Create a horizontal bar chart for multiple-select questions."""
    if not cols or df.empty:
        return create_no_data_figure(title)

    # Count responses for each option (robust to various selection values)
    counts = []
    for col in cols:
        if col in df:
            # Count as selected if value is in ['selected', 'yes', '1', 'true'] (case-insensitive)
            count = df[col].apply(lambda x: str(x).strip().lower() in ["selected", "yes", "1", "true"]).sum()
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
        barmode='group',
        title=title,
        xaxis_title=None,
        yaxis_title="Count",
        margin=dict(l=10, r=10, t=30 if title else 10, b=80),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family=STYLE_VARS["FONT_FAMILY"],
            size=LABEL_FONT_SIZE
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5
        ),
        xaxis=dict(tickangle=-35)
    )

    # Update axes
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
    fig.update_yaxes(showgrid=False)

    return fig

def normalize_colname_for_match(name):
    # Remove all whitespace, punctuation, and lowercase
    name = unicodedata.normalize('NFKD', name)
    name = name.replace('\xa0', ' ')
    name = re.sub(r'\s+', ' ', name)
    name = name.translate(str.maketrans('', '', r'"\'!@#$%^&*()[]{};:,./<>?\\|`~-=+'))
    return name.strip().lower()

def get_best_column_match(target, columns):
    """Return the best matching column from columns for the given target string."""
    norm_target = normalize_colname_for_match(target)
    for col in columns:
        if normalize_colname_for_match(col) == norm_target:
            return col
    # Fallback: partial match
    for col in columns:
        if norm_target in normalize_colname_for_match(col):
            return col
    return None

def generate_grouped_bar_chart(df: pd.DataFrame, cols: List[str], title: Optional[str] = None) -> go.Figure:
    """
    Create a horizontal bar chart for grouped multi-column questions (e.g., regions, barriers).
    Each bar is the count of 'Yes' responses for that option/column.
    """
    if not cols or df.empty:
        return create_no_data_figure(None)
    counts = []
    for col in cols:
        match_col = get_best_column_match(col, df.columns)
        if match_col:
            count = (df[match_col].fillna('').astype(str).str.strip().str.lower() == 'yes').sum()
            # Extract label from column name
            label = simplify_label(col)
            counts.append({'option': label, 'count': count})
    if not counts:
        return create_no_data_figure(None)
    counts_df = pd.DataFrame(counts).sort_values('count', ascending=False)
    # Determine if we need to rotate y-axis labels (not needed for horizontal)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=counts_df['option'],
        x=counts_df['count'],
        orientation='h',
        marker_color=PRIMARY_COLOR,
        text=counts_df['count'],
        textposition='auto',
        hoverinfo='none',
        textfont=dict(size=LABEL_FONT_SIZE)
    ))
    fig.update_layout(
        barmode='group',
        title=None,
        yaxis_title=None,
        xaxis_title="Count",
        margin=dict(l=10, r=10, t=30, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family=STYLE_VARS["FONT_FAMILY"],
            size=LABEL_FONT_SIZE
        ),
        showlegend=False,
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
                # Fall back to bar chart if map creation fails
                return make_bar_chart(df_copy, col, title, horizontal=True)
        else:
            unique_count = df_copy[col].nunique()
            if unique_count <= 5:
                return make_donut_chart(df_copy, col, title)
            else:
                return make_bar_chart(df_copy, col, title, horizontal=True)
    elif chart_type == 'bar':
        return make_bar_chart(df_copy, col, title, horizontal=True)  # Force horizontal
    elif chart_type == 'bar_h':
        return make_bar_chart(df_copy, col, title, horizontal=True)
    elif chart_type == 'histogram':
        if pd.api.types.is_numeric_dtype(df_copy[col]):
            return make_histogram(df_copy, col, title)
        else:
            return make_bar_chart(df_copy, col, title, horizontal=True)
    elif chart_type == 'pie':
        return make_pie_chart(df_copy, col, title)
    elif chart_type == 'donut':
        return make_donut_chart(df_copy, col, title)
    elif chart_type == 'map':
        return make_world_map(df_copy, col, title)
    else:
        return make_bar_chart(df_copy, col, title, horizontal=True)

def make_wordcloud(responses, title=None, width=800, height=400):
    # Combine all responses into a single string
    text = ' '.join([str(r) for r in responses if isinstance(r, str) and r.strip()])
    if not text:
        return create_no_data_figure(title)
    
    wc = WordCloud(width=width, height=height, background_color='white').generate(text)
    img = wc.to_image()
    
    fig = go.Figure()
    fig.add_layout_image(
        dict(
            source=img,  # Pass the PIL Image directly
            xref="paper", yref="paper",
            x=0, y=1, sizex=1, sizey=1,
            sizing="stretch",
            layer="below"
        )
    )
    
    fig.update_layout(
        title=title,
        width=width,
        height=height,
        showlegend=False,
        xaxis=dict(showgrid=False, showticklabels=False, range=[0, 1]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[0, 1]),
        margin=dict(l=0, r=0, t=50, b=0)
    )
    
    return fig

def make_word_freq_bar(responses, title=None, top_n=15, width=800, height=400):
    # Combine all responses into a single string
    text = ' '.join([str(r) for r in responses if isinstance(r, str) and r.strip()])
    if not text:
        return create_no_data_figure(title)
    # Tokenize and clean
    words = re.findall(r'\b\w+\b', text.lower())
    words = [w for w in words if w not in STOPWORDS and len(w) > 2]
    counter = collections.Counter(words)
    most_common = counter.most_common(top_n)
    if not most_common:
        return create_no_data_figure(title)
    labels, values = zip(*most_common)
    fig = go.Figure(go.Bar(
        x=values,
        y=labels,
        orientation='h',
        marker_color=PRIMARY_COLOR,
        text=values,
        textposition='auto',
    ))
    fig.update_layout(
        title=title,
        width=width,
        height=height,
        xaxis_title='Frequency',
        yaxis_title='Word',
        template='plotly_white',
        margin=dict(l=100, r=20, t=40, b=40),
        font=dict(size=13),
    )
    return fig

def generate_task_scale_chart(df: pd.DataFrame, grouped_task_scales: dict) -> go.Figure:
    """Generate a comprehensive task scale chart for all RE phases."""
    from plotly.colors import qualitative
    
    # Collect data from all phases
    all_data = []
    phase_names = []
    
    for phase_key, phase_data in grouped_task_scales.items():
        tasks = phase_data['tasks']
        scales = phase_data['scales']
        
        # For each task, find which scales are present
        for task in tasks:
            task_data = {}
            for scale in scales:
                # Try to find a column for this (task, scale)
                match = None
                for df_col in df.columns:
                    norm_df_col = normalize_colname_for_match(df_col)
                    phase_match = normalize_colname_for_match(f"requirements {phase_key}") in norm_df_col
                    task_match = normalize_colname_for_match(task) in norm_df_col
                    scale_match = normalize_colname_for_match(scale) in norm_df_col
                    if phase_match and task_match and scale_match:
                        match = df_col
                        break
                
                if match and match in df.columns:
                    # Count positive usefulness responses
                    positive_responses = df[match].isin(['Very useful', 'Extremely useful', 'Moderately useful', 'Slightly useful']).sum()
                    task_data[scale] = positive_responses
            
            if task_data:
                all_data.append({
                    'phase': phase_key,
                    'task': task,
                    'data': task_data
                })
    
    if not all_data:
        return create_no_data_figure("No task scale data available")
    
    # Create horizontal grouped bar chart
    fig = go.Figure()
    color_palette = qualitative.Plotly
    
    # Group by phase
    phases = list(grouped_task_scales.keys())
    for i, phase in enumerate(phases):
        phase_data = [d for d in all_data if d['phase'] == phase]
        if not phase_data:
            continue
            
        for j, task_data in enumerate(phase_data):
            task = task_data['task']
            data = task_data['data']
            
            # Use different colors for different scales
            for k, (scale, count) in enumerate(data.items()):
                fig.add_trace(go.Bar(
                    y=[f"{phase}: {task}"],
                    x=[count],
                    name=scale,
                    orientation='h',
                    marker_color=color_palette[k % len(color_palette)],
                    text=[count],
                    textposition='auto',
                    hovertemplate=f'<b>{phase}: {task}</b><br>Scale: {scale}<br>Count: %{{x}}<extra></extra>',
                    legendgroup=scale,
                    showlegend=i == 0  # Only show legend for first phase
                ))
    
    fig.update_layout(
        barmode='stack',
        title="Usefulness/Harmfulness of GenAI for RE Tasks",
        yaxis_title="Task",
        xaxis_title="Count (sum of all positive usefulness responses)",
        showlegend=True,
        legend_title="Scale",
        template="plotly_white",
        height=max(400, len(all_data) * 30),  # Dynamic height based on number of tasks
        font=dict(size=12),
        margin=dict(l=200, r=20, t=40, b=40),  # Increased left margin for long task names
        yaxis=dict(tickfont=dict(size=10), automargin=True),
        xaxis=dict(tickfont=dict(size=10)),
    )
    
    return fig

def make_task_scale_chart(df, phase_key):
    phase = GROUPED_TASK_SCALES[phase_key]
    tasks = phase['tasks']
    
    def normalize_string(s):
        """Improved normalization function that handles HTML entities and extra formatting."""
        if pd.isna(s):
            return ""
        
        s = str(s)
        # Replace HTML entities
        s = s.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&#39;', "'")
        # Remove extra whitespace and normalize
        s = re.sub(r'\s+', ' ', s)
        # Remove punctuation and special characters
        s = re.sub(r'[^\w\s]', '', s)
        # Convert to lowercase
        return s.strip().lower()
    
    task_scale_cols = {task: {'Scale 1': None, 'Scale 2': None} for task in tasks}
    
    for task in tasks:
        norm_task = normalize_string(task)
        for scale_tag in ['Scale 1', 'Scale 2']:
            norm_scale = normalize_string(scale_tag)
            norm_phase = normalize_string(phase_key)
            
            # Try exact match first
            for col in df.columns:
                norm_col = normalize_string(col)
                if (norm_task in norm_col and 
                    norm_phase in norm_col and 
                    norm_scale in norm_col):
                    task_scale_cols[task][scale_tag] = col
                    break
            
            # If no exact match, try partial matching
            if task_scale_cols[task][scale_tag] is None:
                for col in df.columns:
                    norm_col = normalize_string(col)
                    # Check if all components are present (more flexible matching)
                    task_present = any(word in norm_col for word in norm_task.split() if len(word) > 3)
                    phase_present = norm_phase in norm_col
                    scale_present = norm_scale in norm_col
                    
                    if task_present and phase_present and scale_present:
                        task_scale_cols[task][scale_tag] = col
                        break
        
        # Debug print for each task
        print(f"[DEBUG] Phase: {phase_key}, Task: {task}")
        print(f"  Normalized task: '{norm_task}'")
        print(f"  Matched Scale 1 column: {task_scale_cols[task]['Scale 1']}")
        print(f"  Matched Scale 2 column: {task_scale_cols[task]['Scale 2']}")
        
        # Print unique values in matched columns for debugging
        for scale_tag in ['Scale 1', 'Scale 2']:
            col = task_scale_cols[task][scale_tag]
            if col and col in df.columns:
                unique_vals = df[col].dropna().unique()
                print(f"  {scale_tag} unique values: {unique_vals}")
    
    data = {task: {'Useful': 0, 'Harmful': 0} for task in tasks}
    
    # Define expected values more flexibly
    useful_values = ['very useful', 'extremely useful', 'moderately useful', 'slightly useful']
    harmful_values = ['very harmful', 'extremely harmful', 'moderately harmful', 'slightly harmful']
    
    for task in tasks:
        col1 = task_scale_cols[task]['Scale 1']
        col2 = task_scale_cols[task]['Scale 2']
        
        if col1 and col1 in df.columns:
            # Normalize values for comparison
            col_values = df[col1].dropna().astype(str).str.strip().str.lower()
            useful_count = sum(col_values.isin(useful_values))
            data[task]['Useful'] = useful_count
            print(f"[DEBUG] {task} - Scale 1: found {useful_count} useful responses out of {len(col_values)} total")
        
        if col2 and col2 in df.columns:
            # Normalize values for comparison
            col_values = df[col2].dropna().astype(str).str.strip().str.lower()
            harmful_count = sum(col_values.isin(harmful_values))
            data[task]['Harmful'] = harmful_count
            print(f"[DEBUG] {task} - Scale 2: found {harmful_count} harmful responses out of {len(col_values)} total")
    
    if all(v['Useful'] == 0 and v['Harmful'] == 0 for v in data.values()):
        print("[DEBUG] No data found for any task in this phase")
        return create_no_data_figure("No data available for this phase.")
    
    fig = go.Figure()
    tasks_list = list(data.keys())
    useful_vals = [data[task]['Useful'] for task in tasks_list]
    harmful_vals = [data[task]['Harmful'] for task in tasks_list]
    
    fig.add_trace(go.Bar(
        y=tasks_list,
        x=useful_vals,
        name='Useful',
        orientation='h',
        marker_color='#2ca02c',
        text=useful_vals,
        textposition='auto',
        legendgroup='Useful'
    ))
    
    fig.add_trace(go.Bar(
        y=tasks_list,
        x=harmful_vals,
        name='Harmful',
        orientation='h',
        marker_color='#d62728',
        text=harmful_vals,
        textposition='auto',
        legendgroup='Harmful'
    ))
    
    fig.update_layout(
        barmode='group',
        title=None,
        yaxis_title="Task",
        xaxis_title="Count",
        showlegend=True,
        legend_title="Scale",
        template="plotly_white",
        height=500,
        font=dict(size=13),
        margin=dict(l=120, r=20, t=40, b=40),
        yaxis=dict(tickfont=dict(size=12), automargin=True),
        xaxis=dict(tickfont=dict(size=12), tickangle=-15),
    )
    
    return fig 