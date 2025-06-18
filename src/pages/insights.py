"""Insights page module for cross-question analysis."""

import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from plotly.colors import qualitative
import re
from collections import defaultdict
import string

from src.components.charts import (
    generate_chart,
    make_donut_chart,
    make_multi_select_bar,
    make_bar_chart,
    create_no_data_figure,
    make_wordcloud,
    generate_grouped_bar_chart,
    generate_task_scale_chart
)
from src.components.layout import build_stat_card, build_chart_card
from src.config.config import PRIMARY_COLOR, GROUPED_TASK_SCALES, GROUPED_QUESTIONS, INSIGHTS_CHARTS

# Phase key mapping to column phase strings
PHASE_KEY_TO_COLUMN_PHASE = {
    "Elicitation": "requirements elicitation",
    "Analysis & Negotiation": "requirements analysis & negotiation", 
    "Specification / Modeling": "requirements specification / requirements modeling",
    "Validation / Quality Assurance": "requirements validation / quality assurance",
    "Management": "requirements management"
}

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

def normalize_colname(name):
    # Remove all whitespace, punctuation, and lowercase
    name = name.replace('\xa0', ' ')
    name = re.sub(r'\s+', ' ', name)
    name = name.translate(str.maketrans('', '', string.punctuation))
    return name.strip().lower()

def create_awareness_implementation_chart(df: pd.DataFrame) -> go.Figure:
    """Create a chart showing relationship between definition awareness and implementation."""
    # Find awareness column by partial match
    awareness_cols = [col for col in df.columns if "umbrella term" in col]
    if not awareness_cols:
        return create_no_data_figure("Could not find definition awareness column")
    
    # Use the first matching column
    awareness_col = awareness_cols[0]
    implementation_col = "Does your organization incorporate sustainable development practices?"
    
    # Create contingency table
    contingency = pd.crosstab(
        df[awareness_col],
        df[implementation_col],
        normalize='index'
    ) * 100  # Convert to percentages
    
    # Create grouped bar chart
    fig = go.Figure()
    
    for implementation_status in contingency.columns:
        fig.add_trace(go.Bar(
            name=implementation_status,
            x=contingency.index,
            y=contingency[implementation_status],
            text=[f"{val:.1f}%" for val in contingency[implementation_status]],
            textposition='auto',
        ))
    
    fig.update_layout(
        barmode='group',
        title="Relationship between Definition Awareness and Implementation",
        xaxis_title="Familiar with Digital Sustainability Definition",
        yaxis_title="Percentage",
        showlegend=True,
        legend_title="Implementation Status",
        template="plotly_white"
    )
    
    return fig

def create_training_implementation_chart(df: pd.DataFrame) -> go.Figure:
    """Create a chart showing relationship between training participation and implementation."""
    # Cross-tabulate training participation with implementation
    training_col = "Have you participated in one or more training or educational programs on digital sustainability?"
    implementation_col = "Does your organization incorporate sustainable development practices?"
    
    # Create contingency table
    contingency = pd.crosstab(
        df[training_col],
        df[implementation_col],
        normalize='index'
    ) * 100  # Convert to percentages
    
    # Create grouped bar chart
    fig = go.Figure()
    
    for implementation_status in contingency.columns:
        fig.add_trace(go.Bar(
            name=implementation_status,
            x=contingency.index,
            y=contingency[implementation_status],
            text=[f"{val:.1f}%" for val in contingency[implementation_status]],
            textposition='auto',
        ))
    
    fig.update_layout(
        barmode='group',
        title="Relationship between Training Participation and Implementation",
        xaxis_title="Participated in Sustainability Training",
        yaxis_title="Percentage",
        showlegend=True,
        legend_title="Implementation Status",
        template="plotly_white"
    )
    
    return fig

def create_discussion_implementation_chart(df: pd.DataFrame) -> go.Figure:
    """Create a chart showing relationship between discussion frequency and implementation."""
    # Cross-tabulate discussion frequency with implementation
    discussion_col = "How frequently do you encounter (e.g., coming across or taking part in) discussions about digital sustainability in your professional environment?"
    implementation_col = "Does your organization incorporate sustainable development practices?"
    
    # Create contingency table
    contingency = pd.crosstab(
        df[discussion_col],
        df[implementation_col],
        normalize='index'
    ) * 100  # Convert to percentages
    
    # Create grouped bar chart
    fig = go.Figure()
    
    for implementation_status in contingency.columns:
        fig.add_trace(go.Bar(
            name=implementation_status,
            x=contingency.index,
            y=contingency[implementation_status],
            text=[f"{val:.1f}%" for val in contingency[implementation_status]],
            textposition='auto',
        ))
    
    fig.update_layout(
        barmode='group',
        title="Relationship between Discussion Frequency and Implementation",
        xaxis_title="Frequency of Sustainability Discussions",
        yaxis_title="Percentage",
        showlegend=True,
        legend_title="Implementation Status",
        template="plotly_white"
    )
    
    return fig

def create_org_type_sustainability_chart(df: pd.DataFrame) -> go.Figure:
    """Create a chart showing sustainability practices by organization type."""
    org_type_col = "Which of the following organizational types best describes your organization?"
    practices_col = "Does your organization incorporate sustainable development practices?"
    
    # Create contingency table
    contingency = pd.crosstab(
        df[org_type_col],
        df[practices_col],
        normalize='index'
    ) * 100  # Convert to percentages
    
    # Create grouped bar chart
    fig = go.Figure()
    
    for practice_status in contingency.columns:
        fig.add_trace(go.Bar(
            name=practice_status,
            x=contingency.index,
            y=contingency[practice_status],
            text=[f"{val:.1f}%" for val in contingency[practice_status]],
            textposition='auto',
        ))
    
    fig.update_layout(
        barmode='group',
        title="Sustainability Practices by Organization Type",
        xaxis_title="Organization Type",
        yaxis_title="Percentage",
        showlegend=True,
        legend_title="Implementation Status",
        template="plotly_white",
        xaxis={'tickangle': -45}
    )
    
    return fig

def create_org_goals_practices_chart(df: pd.DataFrame) -> go.Figure:
    """Create a chart showing relationship between sustainability goals and practices."""
    goals_col = "Does your organization have specific digital sustainability goals or benchmarks for software development projects?"
    practices_col = "Does your organization incorporate sustainable development practices?"
    
    # Create contingency table
    contingency = pd.crosstab(
        df[goals_col],
        df[practices_col],
        normalize='index'
    ) * 100  # Convert to percentages
    
    # Create grouped bar chart
    fig = go.Figure()
    
    for practice_status in contingency.columns:
        fig.add_trace(go.Bar(
            name=practice_status,
            x=contingency.index,
            y=contingency[practice_status],
            text=[f"{val:.1f}%" for val in contingency[practice_status]],
            textposition='auto',
        ))
    
    fig.update_layout(
        barmode='group',
        title="Impact of Having Sustainability Goals on Implementation",
        xaxis_title="Has Sustainability Goals",
        yaxis_title="Percentage",
        showlegend=True,
        legend_title="Implementation Status",
        template="plotly_white"
    )
    
    return fig

def create_org_csr_practices_chart(df: pd.DataFrame) -> go.Figure:
    """Create a chart showing relationship between having CSR team and practices."""
    csr_col = "Does your organization have a dedicated sustainability or Corporate Social Responsibility (CSR) expert, team or department?"
    practices_col = "Does your organization incorporate sustainable development practices?"
    
    # Create contingency table
    contingency = pd.crosstab(
        df[csr_col],
        df[practices_col],
        normalize='index'
    ) * 100  # Convert to percentages
    
    # Create grouped bar chart
    fig = go.Figure()
    
    for practice_status in contingency.columns:
        fig.add_trace(go.Bar(
            name=practice_status,
            x=contingency.index,
            y=contingency[practice_status],
            text=[f"{val:.1f}%" for val in contingency[practice_status]],
            textposition='auto',
        ))
    
    fig.update_layout(
        barmode='group',
        title="Impact of Having CSR Team on Implementation",
        xaxis_title="Has CSR Team/Expert",
        yaxis_title="Percentage",
        showlegend=True,
        legend_title="Implementation Status",
        template="plotly_white"
    )
    
    return fig

def create_role_implementation_chart(df: pd.DataFrame) -> go.Figure:
    """Create a chart showing sustainability implementation by role."""
    role_col = "Which of the following best describes your current role in the organization?"
    implementation_col = "Do you incorporate digital sustainability considerations in your role-specific tasks?"
    
    # Create contingency table
    contingency = pd.crosstab(
        df[role_col],
        df[implementation_col],
        normalize='index'
    ) * 100  # Convert to percentages
    
    # Create grouped bar chart
    fig = go.Figure()
    
    for impl_status in contingency.columns:
        fig.add_trace(go.Bar(
            name=impl_status,
            x=contingency.index,
            y=contingency[impl_status],
            text=[f"{val:.1f}%" for val in contingency[impl_status]],
            textposition='auto',
        ))
    
    fig.update_layout(
        barmode='group',
        title="Sustainability Implementation by Role",
        xaxis_title="Role",
        yaxis_title="Percentage",
        showlegend=True,
        legend_title="Implementation Status",
        template="plotly_white",
        xaxis={'tickangle': -45}
    )
    
    return fig

def create_role_drivers_chart(df: pd.DataFrame) -> go.Figure:
    """Create a chart showing sustainability drivers by role."""
    role_col = "Which of the following best describes your current role in the organization?"
    
    # Use the exact driver columns from JOB_TASK_MULTI_DRIVES
    driver_cols = [
        'What drives you to incorporate digital sustainability in your role-related tasks?  [Organizational policies ]',
        'What drives you to incorporate digital sustainability in your role-related tasks?  [Personal beliefs ]',
        'What drives you to incorporate digital sustainability in your role-related tasks?  [Client requirements ]',
        'What drives you to incorporate digital sustainability in your role-related tasks?  [User requirements]',
        'What drives you to incorporate digital sustainability in your role-related tasks?  [Legal requirements ]'
    ]
    
    # Verify each driver column exists
    available_driver_cols = []
    for col in driver_cols:
        if col in df.columns:
            available_driver_cols.append(col)
    
    if not available_driver_cols:
        fig = go.Figure()
        fig.update_layout(
            title="No driver data available",
            annotations=[
                dict(
                    text="No data available for drivers analysis",
                    xref="paper",
                    yref="paper",
                    x=0.5,
                    y=0.5,
                    showarrow=False
                )
            ]
        )
        return fig
    
    # Create a mapping for shorter labels
    driver_labels = {
        'Organizational policies ': 'Org Policies',
        'Personal beliefs ': 'Personal Beliefs',
        'Client requirements ': 'Client Requirements',
        'User requirements': 'User Requirements',
        'Legal requirements ': 'Legal Requirements'
    }
    
    # Calculate percentage of each driver by role
    driver_percentages = {}
    for driver_col in available_driver_cols:
        try:
            # Create contingency table for this driver
            contingency = pd.crosstab(
                df[role_col],
                df[driver_col],
                normalize='index'
            ) * 100
            # Get the percentage of "Selected" responses
            if "Selected" in contingency.columns:
                driver_name = driver_col.split('[')[-1].split(']')[0].strip()
                driver_percentages[driver_labels.get(driver_name, driver_name)] = contingency["Selected"]
        except Exception as e:
            continue
    
    if not driver_percentages:
        fig = go.Figure()
        fig.update_layout(
            title="No driver data available",
            annotations=[
                dict(
                    text="No valid data available for drivers analysis",
                    xref="paper",
                    yref="paper",
                    x=0.5,
                    y=0.5,
                    showarrow=False
                )
            ]
        )
        return fig
    
    # Create heatmap
    roles = list(driver_percentages[list(driver_percentages.keys())[0]].index)
    drivers = list(driver_percentages.keys())
    z_values = [[driver_percentages[driver][role] for driver in drivers] for role in roles]
    
    fig = go.Figure(data=go.Heatmap(
        z=z_values,
        x=drivers,
        y=roles,
        colorscale="Viridis",
        text=[[f"{val:.1f}%" for val in row] for row in z_values],
        texttemplate="%{text}",
        textfont={"size": 10},
        textcolor="white",
        showscale=True
    ))
    
    fig.update_layout(
        title="Drivers of Sustainability Implementation by Role",
        xaxis_title="Driver",
        yaxis_title="Role",
        template="plotly_white",
        height=600,
        xaxis={'tickangle': -45}
    )
    
    return fig

def create_role_barriers_chart(df: pd.DataFrame) -> go.Figure:
    """Create a chart showing sustainability barriers by role."""
    role_col = "Which of the following best describes your current role in the organization?"
    
    # Use a subset of barriers for better visualization, with exact column names
    barrier_cols = [
        "What hinders you from incorporating sustainability in your role-specific tasks?\xa0  [Lack of knowledge or awareness (e.g., not knowing enough about sustainability impact or best practices)]",
        "What hinders you from incorporating sustainability in your role-specific tasks?\xa0  [Limited resources or budget (e.g., financial constraints, insufficient tools or technology)]",
        "What hinders you from incorporating sustainability in your role-specific tasks?\xa0  [Insufficient time or competing priorities (e.g., pressing deadlines, other projects taking precedence)]",
        "What hinders you from incorporating sustainability in your role-specific tasks?\xa0  [Lack of organizational or leadership support (e.g., limited buy-in from management, inadequate policy frameworks)]",
        "What hinders you from incorporating sustainability in your role-specific tasks?\xa0  [Complexity or uncertainty of sustainability solutions (e.g., difficulty measuring impact or navigating standards)]"
    ]
    
    # Verify each barrier column exists
    available_barrier_cols = []
    for col in barrier_cols:
        if col in df.columns:
            available_barrier_cols.append(col)
    
    if not available_barrier_cols:
        fig = go.Figure()
        fig.update_layout(
            title="No barrier data available",
            annotations=[
                dict(
                    text="No data available for barriers analysis",
                    xref="paper",
                    yref="paper",
                    x=0.5,
                    y=0.5,
                    showarrow=False
                )
            ]
        )
        return fig
    
    # Create a mapping for shorter labels
    barrier_labels = {
        'Lack of knowledge or awareness (e.g., not knowing enough about sustainability impact or best practices)': 'Knowledge Gap',
        'Limited resources or budget (e.g., financial constraints, insufficient tools or technology)': 'Resource Constraints',
        'Insufficient time or competing priorities (e.g., pressing deadlines, other projects taking precedence)': 'Time Constraints',
        'Lack of organizational or leadership support (e.g., limited buy-in from management, inadequate policy frameworks)': 'Lack of Support',
        'Complexity or uncertainty of sustainability solutions (e.g., difficulty measuring impact or navigating standards)': 'Solution Complexity'
    }
    
    # Calculate percentage of each barrier by role
    barrier_percentages = {}
    for barrier_col in available_barrier_cols:
        try:
            # Create contingency table for this barrier
            contingency = pd.crosstab(
                df[role_col],
                df[barrier_col],
                normalize='index'
            ) * 100
            # Get the percentage of "Selected" responses
            if "Selected" in contingency.columns:
                barrier_name = barrier_col.split('[')[-1].split(']')[0].strip()
                barrier_percentages[barrier_labels.get(barrier_name, barrier_name)] = contingency["Selected"]
        except Exception as e:
            continue
    
    if not barrier_percentages:
        fig = go.Figure()
        fig.update_layout(
            title="No barrier data available",
            annotations=[
                dict(
                    text="No valid data available for barriers analysis",
                    xref="paper",
                    yref="paper",
                    x=0.5,
                    y=0.5,
                    showarrow=False
                )
            ]
        )
        return fig
    
    # Create heatmap
    roles = list(barrier_percentages[list(barrier_percentages.keys())[0]].index)
    barriers = list(barrier_percentages.keys())
    z_values = [[barrier_percentages[barrier][role] for barrier in barriers] for role in roles]
    
    fig = go.Figure(data=go.Heatmap(
        z=z_values,
        x=barriers,
        y=roles,
        colorscale="Viridis",
        text=[[f"{val:.1f}%" for val in row] for row in z_values],
        texttemplate="%{text}",
        textfont={"size": 10},
        textcolor="white",
        showscale=True
    ))
    
    fig.update_layout(
        title="Barriers to Sustainability Implementation by Role",
        xaxis_title="Barrier",
        yaxis_title="Role",
        template="plotly_white",
        height=600,
        xaxis={'tickangle': -45}
    )
    
    return fig

def create_barriers_by_org_type_chart(df: pd.DataFrame) -> go.Figure:
    """Create a heatmap showing barriers by organization type."""
    org_type_col = "Which of the following organizational types best describes your organization?"
    
    # Use the same barrier columns as in create_role_barriers_chart
    barrier_cols = [
        "What hinders you from incorporating sustainability in your role-specific tasks?\xa0  [Lack of knowledge or awareness (e.g., not knowing enough about sustainability impact or best practices)]",
        "What hinders you from incorporating sustainability in your role-specific tasks?\xa0  [Limited resources or budget (e.g., financial constraints, insufficient tools or technology)]",
        "What hinders you from incorporating sustainability in your role-specific tasks?\xa0  [Insufficient time or competing priorities (e.g., pressing deadlines, other projects taking precedence)]",
        "What hinders you from incorporating sustainability in your role-specific tasks?\xa0  [Lack of organizational or leadership support (e.g., limited buy-in from management, inadequate policy frameworks)]",
        "What hinders you from incorporating sustainability in your role-specific tasks?\xa0  [Complexity or uncertainty of sustainability solutions (e.g., difficulty measuring impact or navigating standards)]"
    ]
    
    # Create a mapping for shorter labels
    barrier_labels = {
        'Lack of knowledge or awareness (e.g., not knowing enough about sustainability impact or best practices)': 'Knowledge Gap',
        'Limited resources or budget (e.g., financial constraints, insufficient tools or technology)': 'Resource Constraints',
        'Insufficient time or competing priorities (e.g., pressing deadlines, other projects taking precedence)': 'Time Constraints',
        'Lack of organizational or leadership support (e.g., limited buy-in from management, inadequate policy frameworks)': 'Lack of Support',
        'Complexity or uncertainty of sustainability solutions (e.g., difficulty measuring impact or navigating standards)': 'Solution Complexity'
    }
    
    # Calculate percentage of each barrier by organization type
    barrier_percentages = {}
    for barrier_col in barrier_cols:
        try:
            # Create contingency table for this barrier
            contingency = pd.crosstab(
                df[org_type_col],
                df[barrier_col],
                normalize='index'
            ) * 100
            # Get the percentage of "Selected" responses
            if "Selected" in contingency.columns:
                barrier_name = barrier_col.split('[')[-1].split(']')[0].strip()
                barrier_percentages[barrier_labels.get(barrier_name, barrier_name)] = contingency["Selected"]
        except Exception as e:
            continue
    
    if not barrier_percentages:
        return create_no_data_figure("No barrier data available")
    
    # Create heatmap
    org_types = list(barrier_percentages[list(barrier_percentages.keys())[0]].index)
    barriers = list(barrier_percentages.keys())
    z_values = [[barrier_percentages[barrier][org_type] for barrier in barriers] for org_type in org_types]
    
    fig = go.Figure(data=go.Heatmap(
        z=z_values,
        x=barriers,
        y=org_types,
        colorscale="Viridis",
        text=[[f"{val:.1f}%" for val in row] for row in z_values],
        texttemplate="%{text}",
        textfont={"size": 10},
        textcolor="white",
        showscale=True
    ))
    
    fig.update_layout(
        title="Barriers by Organization Type",
        xaxis_title="Barrier",
        yaxis_title="Organization Type",
        template="plotly_white",
        height=600,
        xaxis={'tickangle': -45}
    )
    
    return fig

def create_drivers_by_org_type_chart(df: pd.DataFrame) -> go.Figure:
    """Create a heatmap showing drivers by organization type."""
    org_type_col = "Which of the following organizational types best describes your organization?"
    
    # Use the same driver columns as in create_role_drivers_chart
    driver_cols = [
        'What drives you to incorporate digital sustainability in your role-related tasks?  [Organizational policies ]',
        'What drives you to incorporate digital sustainability in your role-related tasks?  [Personal beliefs ]',
        'What drives you to incorporate digital sustainability in your role-related tasks?  [Client requirements ]',
        'What drives you to incorporate digital sustainability in your role-related tasks?  [User requirements]',
        'What drives you to incorporate digital sustainability in your role-related tasks?  [Legal requirements ]'
    ]
    
    # Create a mapping for shorter labels
    driver_labels = {
        'Organizational policies ': 'Org Policies',
        'Personal beliefs ': 'Personal Beliefs',
        'Client requirements ': 'Client Requirements',
        'User requirements': 'User Requirements',
        'Legal requirements ': 'Legal Requirements'
    }
    
    # Calculate percentage of each driver by organization type
    driver_percentages = {}
    for driver_col in driver_cols:
        try:
            # Create contingency table for this driver
            contingency = pd.crosstab(
                df[org_type_col],
                df[driver_col],
                normalize='index'
            ) * 100
            # Get the percentage of "Selected" responses
            if "Selected" in contingency.columns:
                driver_name = driver_col.split('[')[-1].split(']')[0].strip()
                driver_percentages[driver_labels.get(driver_name, driver_name)] = contingency["Selected"]
        except Exception as e:
            continue
    
    if not driver_percentages:
        return create_no_data_figure("No driver data available")
    
    # Create heatmap
    org_types = list(driver_percentages[list(driver_percentages.keys())[0]].index)
    drivers = list(driver_percentages.keys())
    z_values = [[driver_percentages[driver][org_type] for driver in drivers] for org_type in org_types]
    
    fig = go.Figure(data=go.Heatmap(
        z=z_values,
        x=drivers,
        y=org_types,
        colorscale="Viridis",
        text=[[f"{val:.1f}%" for val in row] for row in z_values],
        texttemplate="%{text}",
        textfont={"size": 10},
        textcolor="white",
        showscale=True
    ))
    
    fig.update_layout(
        title="Drivers by Organization Type",
        xaxis_title="Driver",
        yaxis_title="Organization Type",
        template="plotly_white",
        height=600,
        xaxis={'tickangle': -45}
    )
    
    return fig

def create_barriers_drivers_correlation_chart(df: pd.DataFrame) -> go.Figure:
    """Create a correlation heatmap between barriers and drivers."""
    # Get barrier and driver columns
    barrier_cols = [col for col in df.columns if "hinder" in col.lower() and "[" in col]
    driver_cols = [col for col in df.columns if "drive" in col.lower() and "[" in col]
    
    if not barrier_cols or not driver_cols:
        return create_no_data_figure("No barrier/driver data available")
    
    # Create binary matrices for barriers and drivers
    barrier_matrix = df[barrier_cols].fillna(0).astype(bool).astype(int)
    driver_matrix = df[driver_cols].fillna(0).astype(bool).astype(int)
    
    # Calculate correlation matrix
    correlation_matrix = pd.DataFrame(index=barrier_cols, columns=driver_cols)
    for barrier in barrier_cols:
        for driver in driver_cols:
            correlation = np.corrcoef(barrier_matrix[barrier], driver_matrix[driver])[0, 1]
            correlation_matrix.loc[barrier, driver] = correlation
    
    # Simplify labels
    barrier_labels = [col.split('[')[-1].split(']')[0].strip() for col in barrier_cols]
    driver_labels = [col.split('[')[-1].split(']')[0].strip() for col in driver_cols]
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=driver_labels,
        y=barrier_labels,
        colorscale="RdBu",
        zmid=0,
        text=[[f"{val:.2f}" for val in row] for row in correlation_matrix.values],
        texttemplate="%{text}",
        textfont={"size": 10, "color": "black"},
        showscale=True
    ))
    
    fig.update_layout(
        title="Correlation between Barriers and Drivers",
        xaxis_title="Drivers",
        yaxis_title="Barriers",
        template="plotly_white",
        height=600,
        xaxis={'tickangle': -45}
    )
    
    return fig

def make_task_scale_chart(df, phase_key):
    phase = GROUPED_TASK_SCALES[phase_key]
    tasks = phase['tasks']
    
    def normalize_string(s):
        if pd.isna(s):
            return ""
        s = str(s)
        s = s.replace('and goals ', '')
        s = s.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&#39;', "'")
        s = re.sub(r'\s+', ' ', s)
        s = re.sub(r'[^\w\s]', '', s)
        return s.strip().lower()
    
    task_scale_cols = {task: {'Scale 1': None, 'Scale 2': None} for task in tasks}
    
    for task in tasks:
        norm_task = normalize_string(task)
        for scale_tag in ['Scale 1', 'Scale 2']:
            norm_scale = normalize_string(scale_tag)
            norm_phase = normalize_string(PHASE_KEY_TO_COLUMN_PHASE.get(phase_key, phase_key))
            for col in df.columns:
                norm_col = normalize_string(col)
                if (norm_task in norm_col and 
                    norm_phase in norm_col and 
                    norm_scale in norm_col):
                    task_scale_cols[task][scale_tag] = col
                    break
            if task_scale_cols[task][scale_tag] is None:
                for col in df.columns:
                    norm_col = normalize_string(col)
                    task_present = any(word in norm_col for word in norm_task.split() if len(word) > 3)
                    phase_present = norm_phase in norm_col
                    scale_present = norm_scale in norm_col
                    if task_present and phase_present and scale_present:
                        task_scale_cols[task][scale_tag] = col
                        break
    
    data = {task: {'Useful': 0, 'Harmful': 0} for task in tasks}
    useful_values = ['very useful', 'extremely useful', 'moderately useful', 'slightly useful']
    harmful_values = ['very harmful', 'extremely harmful', 'moderately harmful', 'slightly harmful']
    
    for task in tasks:
        col1 = task_scale_cols[task]['Scale 1']
        col2 = task_scale_cols[task]['Scale 2']
        if col1 and col1 in df.columns:
            col_values = df[col1].dropna().astype(str).str.strip().str.lower()
            useful_count = sum(col_values.isin(useful_values))
            data[task]['Useful'] = useful_count
        if col2 and col2 in df.columns:
            col_values = df[col2].dropna().astype(str).str.strip().str.lower()
            harmful_count = sum(col_values.isin(harmful_values))
            data[task]['Harmful'] = harmful_count
    
    if all(v['Useful'] == 0 and v['Harmful'] == 0 for v in data.values()):
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
        font=dict(size=15),
        margin=dict(l=120, r=20, t=40, b=40),
        yaxis=dict(tickfont=dict(size=18), automargin=True),
        xaxis=dict(tickfont=dict(size=14), tickangle=-15),
    )
    
    return fig

def build_insights_page(df: pd.DataFrame) -> html.Div:
    """Build the insights page layout with cross-question analysis."""
    # Single-value insight charts
    single_charts = []
    for col in INSIGHTS_CHARTS:
        if col not in df.columns:
            continue
        fig = generate_chart(df, col, chart_type='bar_h')  # Force horizontal
        question_text = col.strip()
        if question_text.endswith('?'):
            question_text = question_text[:-1]
        single_charts.append(html.Div([
            html.H5(question_text, className="mb-3", style={"color": PRIMARY_COLOR, "fontWeight": 600, "fontSize": "1.25rem"}),
            build_chart_card("", fig, 12)
        ]))

    # Grouped training preferences
    training_group = GROUPED_QUESTIONS["training_preferences"]
    training_fig = generate_grouped_bar_chart(df, training_group['columns'], None)  # horizontal by default

    # Task scale charts for each phase
    task_scale_charts = []
    for phase_key in GROUPED_TASK_SCALES.keys():
        fig = make_task_scale_chart(df, phase_key)
        phase_name = phase_key.replace('_', ' ').title()
        task_scale_charts.append(html.Div([
            html.H5(f"Usefulness/Harmfulness for {phase_name}", className="mb-3", style={"color": PRIMARY_COLOR, "fontWeight": 600, "fontSize": "1.25rem"}),
            build_chart_card("", fig, 12)
        ]))

    return html.Div([
        html.H3("Key Insights", className="mb-4 mt-2", style=SECTION_HEADER_STYLE),
        html.Div([
            html.H4("Single-Choice Insights", className="mb-3", style=SECTION_HEADER_STYLE),
            *single_charts
        ]),
        html.Div([
            html.H4("Training Preferences", className="mb-3", style=SECTION_HEADER_STYLE),
            html.H5("Which training format would you prefer?", className="mb-3", style={"color": PRIMARY_COLOR, "fontWeight": 600, "fontSize": "1.25rem"}),
            build_chart_card("", training_fig, 12)
        ]),
        html.Div([
            html.H4("Usefulness/Harmfulness of GenAI for RE Tasks", className="mb-3", style=SECTION_HEADER_STYLE),
            *task_scale_charts
        ])
    ]) 