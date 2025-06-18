"""Configuration for GenAI in RE Survey Dashboard"""

# File path for the survey data
DATA_FILE = "data/2025.csv"

# Column groupings for logical dashboard sections

DEMOGRAPHIC_COLS = [
    "Which of the following organization / business types best describes your organization?",
    "Which of the following organization / business types best describes your organization? [Other]",
    "How many years of professional experience do you have in Requirements Engineering (RE)?",
    "What is your current role or position in your organization? [Business Analyst]",
    "What is your current role or position in your organization? [Product Owner]",
    "What is your current role or position in your organization? [Requirements Engineer]",
    "What is your current role or position in your organization? [Software Architect]",
    "What is your current role or position in your organization? [UI / UX Designer]",
    "What is your current role or position in your organization? [Software Developer]",
    "What is your current role or position in your organization? [Technical Leader]",
    "What is your current role or position in your organization? [Project Manager]",
    "What is your current role or position in your organization? [Other]",
    "In which of the following regions do you typically work? [Europe]",
    "In which of the following regions do you typically work? [Asia]",
    "In which of the following regions do you typically work? [Africa]",
    "In which of the following regions do you typically work? [North America]",
    "In which of the following regions do you typically work? [South America]",
    "In which of the following regions do you typically work? [Australia - New Zealand (Oceania)]",
]

APPLICATION_DOMAIN_COLS = [
    col for col in [
        "In which application domain(s) have you worked over the past 5 years? [Aerospace]",
        "In which application domain(s) have you worked over the past 5 years? [Automotive]",
        "In which application domain(s) have you worked over the past 5 years? [Banking / Insurances ]",
        "In which application domain(s) have you worked over the past 5 years? [Chemicals, pharmaceuticals, medical technology]",
        "In which application domain(s) have you worked over the past 5 years? [Defense]",
        "In which application domain(s) have you worked over the past 5 years? [Education]",
        "In which application domain(s) have you worked over the past 5 years? [IT / Software]",
        "In which application domain(s) have you worked over the past 5 years? [Mechanical Engineering]",
        "In which application domain(s) have you worked over the past 5 years? [Research]",
        "In which application domain(s) have you worked over the past 5 years? [Telecommunication]",
        "In which application domain(s) have you worked over the past 5 years? [Trade]",
        "In which application domain(s) have you worked over the past 5 years? [Transport & Logistics]",
        "In which application domain(s) have you worked over the past 5 years? [Other]",
    ]
]

RE_EXPERIENCE_COLS = [
    "Please assess your knowledge / experience in the various RE-related disciplines on the following scale:   \tNo Experience - I have no experience in this area \tBeginner - I have some basic knowledge but little practical experience \tIntermediate - I have practical experience and can perform tasks with some guidance \tAdvanced - I have substantial experience and can perform tasks independently \tExpert - I have deep expertise and can guide others or develop new approaches   [Requirements Elicitation]",
    "Please assess your knowledge / experience in the various RE-related disciplines on the following scale:   \tNo Experience - I have no experience in this area \tBeginner - I have some basic knowledge but little practical experience \tIntermediate - I have practical experience and can perform tasks with some guidance \tAdvanced - I have substantial experience and can perform tasks independently \tExpert - I have deep expertise and can guide others or develop new approaches   [Requirements Analysis & Negotiation]",
    "Please assess your knowledge / experience in the various RE-related disciplines on the following scale:   \tNo Experience - I have no experience in this area \tBeginner - I have some basic knowledge but little practical experience \tIntermediate - I have practical experience and can perform tasks with some guidance \tAdvanced - I have substantial experience and can perform tasks independently \tExpert - I have deep expertise and can guide others or develop new approaches   [Requirements Specification / Requirements Modeling]",
    "Please assess your knowledge / experience in the various RE-related disciplines on the following scale:   \tNo Experience - I have no experience in this area \tBeginner - I have some basic knowledge but little practical experience \tIntermediate - I have practical experience and can perform tasks with some guidance \tAdvanced - I have substantial experience and can perform tasks independently \tExpert - I have deep expertise and can guide others or develop new approaches   [Requirements Validation / Quality Assurance]",
    "Please assess your knowledge / experience in the various RE-related disciplines on the following scale:   \tNo Experience - I have no experience in this area \tBeginner - I have some basic knowledge but little practical experience \tIntermediate - I have practical experience and can perform tasks with some guidance \tAdvanced - I have substantial experience and can perform tasks independently \tExpert - I have deep expertise and can guide others or develop new approaches   [Requirements Management]",
]

GENAI_USAGE_COLS = [
    "How long have you been working in the field of GenAI?",
    "How often do you use ChatGPT or similar AI chatbots?",
    "How often do you use ChatGPT or similar AI chatbots? [Other]",
    "Have you already used / applied GenAI for RE-related disciplines in your professional work?",
]

GENAI_RE_DISCIPLINE_COLS = [
    "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Elicitation]",
    "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Elicitation][Comment]",
    "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Analysis & Negotiation]",
    "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Analysis & Negotiation][Comment]",
    "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Specification / Requirements Modeling]",
    "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Specification / Requirements Modeling][Comment]",
    "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Validation / Quality Assurance]",
    "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Validation / Quality Assurance][Comment]",
    "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Management]",
    "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Management][Comment]",
    "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Other]",
    "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Other comment]",
]

BARRIERS_COLS = [
    "Have you also experienced situations that prevented you from using GenAI in RE-related disciplines? ",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Lack of awareness or knowledge]",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Lack of support / tools]",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Lack of time]",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Insufficient quality / availability of input data ]",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Unclear, inconsistent, low-quality results]",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Uncertainty about ROI (Return on Investment)]",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Unclear or inconsistent results]",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Cultural resistance and organizational inertia]",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Using AI is forbidden by my organization]",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Ethical and legal concerns (e.g., data privacy)]",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Limited scope of AI applications in RE]",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Fear of job displacement]",
    "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Other]",
]

# ... (other groupings for tasks, threats, training, comments can be added similarly)

# Color and style variables (reuse from previous config if needed)
STYLE_VARS = {
    "PRIMARY_COLOR": "#831E82",
    "SECONDARY_COLOR": "#A450A3",
    "TERTIARY_COLOR": "#C581C4",
    "QUATERNARY_COLOR": "#E6B3E5",
    "BACKGROUND_COLOR": "#f8f9fa",
    "CARD_HEADER_COLOR": "#831E82",
    "FONT_FAMILY": "Helvetica",
    "FONT_SIZE": 14,
    "CARD_MARGIN": "mb-4",
    "ROW_MARGIN": "mb-5 g-4",
}
PRIMARY_COLOR = STYLE_VARS["PRIMARY_COLOR"]

# Sidebar style
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": STYLE_VARS["PRIMARY_COLOR"],
    "color": "white",
    "overflow-y": "auto"
}

CONTENT_STYLE = {
    "margin-left": "22rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": STYLE_VARS["BACKGROUND_COLOR"],
}

# Grouped multi-column questions for single-chart rendering
GROUPED_QUESTIONS = {
    "regions": {
        "question": "In which of the following regions do you typically work?",
        "columns": [
            "In which of the following regions do you typically work? [Europe]",
            "In which of the following regions do you typically work? [Asia]",
            "In which of the following regions do you typically work? [Africa]",
            "In which of the following regions do you typically work? [North America]",
            "In which of the following regions do you typically work? [South America]",
            "In which of the following regions do you typically work? [Australia - New Zealand (Oceania)]",
        ],
    },
    "application_domains": {
        "question": "In which application domain(s) have you worked over the past 5 years?",
        "columns": APPLICATION_DOMAIN_COLS,
    },
    "roles": {
        "question": "What is your current role or position in your organization?",
        "columns": [
            "What is your current role or position in your organization? [Business Analyst]",
            "What is your current role or position in your organization? [Product Owner]",
            "What is your current role or position in your organization? [Requirements Engineer]",
            "What is your current role or position in your organization? [Software Architect]",
            "What is your current role or position in your organization? [UI / UX Designer]",
            "What is your current role or position in your organization? [Software Developer]",
            "What is your current role or position in your organization? [Technical Leader]",
            "What is your current role or position in your organization? [Project Manager]",
            "What is your current role or position in your organization? [Other]",
        ],
    },
    "barriers": {
        "question": "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work?",
        "columns": [
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Lack of awareness or knowledge]",
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Lack of support / tools]",
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Lack of time]",
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Insufficient quality / availability of input data ]",
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Unclear, inconsistent, low-quality results]",
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Uncertainty about ROI (Return on Investment)]",
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Unclear or inconsistent results]",
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Cultural resistance and organizational inertia]",
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Using AI is forbidden by my organization]",
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Ethical and legal concerns (e.g., data privacy)]",
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Limited scope of AI applications in RE]",
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Fear of job displacement]",
            "What reasons prevent(ed) you from using GenAI in RE-related disciplines in your professional work? [Other]",
        ],
    },
    "genai_re_disciplines": {
        "question": "For which of the following RE-related disciplines did you use / apply GenAI?",
        "columns": [
            "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Elicitation]",
            "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Analysis & Negotiation]",
            "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Specification / Requirements Modeling]",
            "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Validation / Quality Assurance]",
            "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Management]",
            "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Other]",
        ],
    },
}

# Year selection for multi-year support
AVAILABLE_YEARS = [2025]  # Add more years as needed, e.g., 2024
YEAR_TO_FILE = {
    2025: "data/2025.csv",
    # 2024: "data/2024.csv",
}

GROUPED_TASK_SCALES = {
    "elicitation": {
        "question": "Usefulness/Harmfulness of GenAI for Requirements Elicitation Tasks",
        "tasks": [
            "Analysis of elicited data(e.g., gained from interviews, surveys, field studies,document analysis)",
            "Creativity / ideation(e.g., generating (innovative) ideas / requirements)",
            "Performing domain analysis",
            "Identification / analysis of stakeholders and their needs(e.g., generating personas)",
            "Analysis of as-is situations / as-is scenarios",
            "Preparation of surveys / interview guidelines",
            "Preparation of workshops / focus groups",
            "Preparation of field studies / observations",
            "Prototyping for requirements elicitation",
        ],
        "scales": ["Scale 1", "Scale 2"],
    },
    "analysis": {
        "question": "Usefulness/Harmfulness of GenAI for Requirements Analysis & Negotiation Tasks",
        "tasks": [
            "Requirements prioritization",
            "Conflict identification and resolution",
            "Feasibility analysis / Risk analysis",
            "Requirements refinement and clarfication",
            "Stakeholder alignment and consensus building",
            "Requirements categorization and grouping",
            "Trade-off analysis",
            "Gap analysis",
            "Change impact analysis",
        ],
        "scales": ["Scale 1", "Scale 2"],
    },
    "specification": {
        "question": "Usefulness/Harmfulness of GenAI for Requirements Specification / Modeling Tasks",
        "tasks": [
            "Creating document structures",
            "Drafting specifications",
            "Formulating requirements",
            "Creating use case descriptions",
            "Creating diagrams (e.g., UML models)",
            "Defining acceptance criteria",
        ],
        "scales": ["Scale 1", "Scale 2"],
    },
    "validation": {
        "question": "Usefulness/Harmfulness of GenAI for Requirements Validation / Quality Assurance Tasks",
        "tasks": [
            "Validation against business objectives",
            "Validation against stakeholder needs",
            "Creation of test cases(e.g., to verify testability)",
            "Identification of inconsistencies",
            "Identification of unnecessary / incorrect requirements",
            "Identification of incomplete / missing requirements",
            "Identification of requirements that are difficult to understand(e.g., due to ambiguities)",
            "Planning and conducting reviews or inspections",
        ],
        "scales": ["Scale 1", "Scale 2"],
    },
    "management": {
        "question": "Usefulness/Harmfulness of GenAI for Requirements Management Tasks",
        "tasks": [
            "Maintain requirements traceabilty",
            "Change management",
            "Configuration management (e.g., version control, document management)",
            "Requirements tracking and monitoring",
            "Requirements process assessment(e.g., auditing)",
        ],
        "scales": ["Scale 1", "Scale 2"],
    },
} 