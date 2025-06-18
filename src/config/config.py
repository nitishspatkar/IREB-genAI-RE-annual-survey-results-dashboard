# Centralized style and color variables
STYLE_VARS = {
    "PRIMARY_COLOR": "#831E82",
    "SECONDARY_COLOR": "#A450A3",
    "TERTIARY_COLOR": "#C581C4",
    "QUATERNARY_COLOR": "#E6B3E5",
    "BACKGROUND_COLOR": "#f8f9fa",
    "CARD_HEADER_COLOR": "#831E82",
    "FONT_FAMILY": "Helvetica",
    "FONT_SIZE": 20,
    "CARD_MARGIN": "mb-4",
    "ROW_MARGIN": "mb-5 g-4",
}
PRIMARY_COLOR = STYLE_VARS["PRIMARY_COLOR"]

# Main content style for the dashboard
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "0rem",
    "padding": "2rem 2rem",
    "background": STYLE_VARS["BACKGROUND_COLOR"],
    "min-height": "100vh"
}

# Sidebar style for navigation
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "border-right": "1px solid #dee2e6",
    "overflow-y": "auto"
}

# Data year mapping (update as new years are added)
YEAR_TO_FILE = {
    2025: "data/2025.csv",
    2026: "data/2026.csv",
}
AVAILABLE_YEARS = sorted(YEAR_TO_FILE.keys())

# Demographic columns (actual column names from CSV)
DEMOGRAPHIC_COLS = [
    "Which of the following organization / business types best describes your organization?",
    "Which of the following organization / business types best describes your organization? [Other]",
    "How many years of professional experience do you have in Requirements Engineering (RE)? ",
    "What is your current role or position in your organization?  [Business Analyst]",
    "What is your current role or position in your organization?  [Product Owner]",
    "What is your current role or position in your organization?  [Requirements Engineer]",
    "What is your current role or position in your organization?  [Software Architect]",
    "What is your current role or position in your organization?  [UI / UX Designer]",
    "What is your current role or position in your organization?  [Software Developer]",
    "What is your current role or position in your organization?  [Technical Leader]",
    "What is your current role or position in your organization?  [Project Manager]",
    "What is your current role or position in your organization?  [Other]",
    "In which of the following regions do you typically work? [Europe]",
    "In which of the following regions do you typically work? [Asia]",
    "In which of the following regions do you typically work? [Africa]",
    "In which of the following regions do you typically work? [North America]",
    "In which of the following regions do you typically work? [South America]",
    "In which of the following regions do you typically work? [Australia - New Zealand (Oceania)]",
]

# Application domain columns
APPLICATION_DOMAIN_COLS = [
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

# RE Experience columns
RE_EXPERIENCE_COLS = [
    "Please assess your knowledge / experience in the various RE-related disciplines on the following scale:   	No Experience - I have no experience in this area 	Beginner - I have some basic knowledge but little practical experience 	Intermediate - I have practical experience and can perform tasks with some guidance 	Advanced - I have substantial experience and can perform tasks independently 	Expert - I have deep expertise and can guide others or develop new approaches   [Requirements Elicitation]",
    "Please assess your knowledge / experience in the various RE-related disciplines on the following scale:   	No Experience - I have no experience in this area 	Beginner - I have some basic knowledge but little practical experience 	Intermediate - I have practical experience and can perform tasks with some guidance 	Advanced - I have substantial experience and can perform tasks independently 	Expert - I have deep expertise and can guide others or develop new approaches   [Requirements Analysis & Negotiation]",
    "Please assess your knowledge / experience in the various RE-related disciplines on the following scale:   	No Experience - I have no experience in this area 	Beginner - I have some basic knowledge but little practical experience 	Intermediate - I have practical experience and can perform tasks with some guidance 	Advanced - I have substantial experience and can perform tasks independently 	Expert - I have deep expertise and can guide others or develop new approaches   [Requirements Specification / Requirements Modeling]",
    "Please assess your knowledge / experience in the various RE-related disciplines on the following scale:   	No Experience - I have no experience in this area 	Beginner - I have some basic knowledge but little practical experience 	Intermediate - I have practical experience and can perform tasks with some guidance 	Advanced - I have substantial experience and can perform tasks independently 	Expert - I have deep expertise and can guide others or develop new approaches   [Requirements Validation / Quality Assurance]",
    "Please assess your knowledge / experience in the various RE-related disciplines on the following scale:   	No Experience - I have no experience in this area 	Beginner - I have some basic knowledge but little practical experience 	Intermediate - I have practical experience and can perform tasks with some guidance 	Advanced - I have substantial experience and can perform tasks independently 	Expert - I have deep expertise and can guide others or develop new approaches   [Requirements Management]",
]

# GenAI Usage columns
GENAI_USAGE_COLS = [
    "How long have you been working in the field of GenAI? ",
    "How often do you use ChatGPT or similar AI chatbots? ",
    "How often do you use ChatGPT or similar AI chatbots?  [Other]",
    "Have you already used / applied GenAI for RE-related disciplines in your professional work?",
]

# GenAI RE Discipline columns
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

# Barriers columns
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

# Training preferences columns
JOB_TASK_MULTI_DRIVES = [
    "For which of the following activities would you like to receive trainings (if any)?For each activity you selected, please provide examples of training topics that would interest you. [AI-supported Requirements Elicitation]",
    "For which of the following activities would you like to receive trainings (if any)?For each activity you selected, please provide examples of training topics that would interest you. [AI-supported Requirements Analysis & Negotiation]",
    "For which of the following activities would you like to receive trainings (if any)?For each activity you selected, please provide examples of training topics that would interest you. [AI-supported Requirements Specification / Requirements Modeling]",
    "For which of the following activities would you like to receive trainings (if any)?For each activity you selected, please provide examples of training topics that would interest you. [AI-supported Requirements Validation / Quality Assurance]",
    "For which of the following activities would you like to receive trainings (if any)?For each activity you selected, please provide examples of training topics that would interest you. [AI-supported Requirements Management]",
    "For which of the following activities would you like to receive trainings (if any)?For each activity you selected, please provide examples of training topics that would interest you. [Other]",
]

# Training format preferences
JOB_TASK_MULTI_HINDER = [
    "Which training format would you prefer? You can select up to three training formats.  [\"Classical Training\" (e.g., Classroom Training, Face-2-Face Training)]",
    "Which training format would you prefer? You can select up to three training formats.  [Community of practice]",
    "Which training format would you prefer? You can select up to three training formats.  [Newsletter]",
    "Which training format would you prefer? You can select up to three training formats.  [Workshops, tutorials and hands-on labs]",
    "Which training format would you prefer? You can select up to three training formats.  [Online courses and webinars]",
    "Which training format would you prefer? You can select up to three training formats.  [Mentoring programs]",
    "Which training format would you prefer? You can select up to three training formats.  [Blended learning programs]",
    "Which training format would you prefer? You can select up to three training formats.  [Case study analysis and group discussions]",
    "Which training format would you prefer? You can select up to three training formats.  [Conferences ]",
    "Which training format would you prefer? You can select up to three training formats.  [Hackathons]",
    "Which training format would you prefer? You can select up to three training formats.  [Other]",
]

# Threats/limitations columns
JOB_TASK_MULTI_KNOWLEDGE = [
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Data quality and availability]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Bias in AI models]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Lack of transparency and explainability]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Over-reliance on AI]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Contextual understanding and ambiguity handling]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Ethical and legal concerns]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Integration challenges (i.e., integrating AI in existing RE processes)]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Maintenance and adaptation (i.e., keeping the AI models up to date)]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Loss of human intuition and judgement]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Resistance to adoption]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Scalability issues]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Cost and ressource constraints]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Hallucinations(i.e., generated output that is nonsensical, inaccurate or not based on training data)]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Confidentiality]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [I don't see any limitations / threats]",
    "In the following, you find a list of limitation / threats. Please select up to three limitations / threats that you see concerning AI in RE? [Other]",
]

# Skills change question
JOB_TASK_MULTI_SUPPORT = [
    "Do you think the skill set of requirements engineers will need to change as AI becomes more prevalent in requirements engineering?If yes, please specify which skills you believe will be affected or will need to change in the comments field.   ",
    "Do you think the skill set of requirements engineers will need to change as AI becomes more prevalent in requirements engineering?If yes, please specify which skills you believe will be affected or will need to change in the comments field.    [Comment]",
]

# Insights charts (single-choice questions for insights page)
INSIGHTS_CHARTS = [
    "Do you think the skill set of requirements engineers will need to change as AI becomes more prevalent in requirements engineering?If yes, please specify which skills you believe will be affected or will need to change in the comments field.   ",
    "How long have you been working in the field of GenAI? ",
    "How often do you use ChatGPT or similar AI chatbots? ",
    "Have you already used / applied GenAI for RE-related disciplines in your professional work?",
    "Have you also experienced situations that prevented you from using GenAI in RE-related disciplines? ",
]

# Open-ended response columns
OPEN_ENDED_COLS = [
    "Do you think the skill set of requirements engineers will need to change as AI becomes more prevalent in requirements engineering?If yes, please specify which skills you believe will be affected or will need to change in the comments field.    [Comment]",
]

# Grouped questions for multi-select visualization
GROUPED_QUESTIONS = {
    "regions": {
        "question": "Which regions do you work in?",
        "columns": [
            "In which of the following regions do you typically work? [Europe]",
            "In which of the following regions do you typically work? [Asia]",
            "In which of the following regions do you typically work? [Africa]",
            "In which of the following regions do you typically work? [North America]",
            "In which of the following regions do you typically work? [South America]",
            "In which of the following regions do you typically work? [Australia - New Zealand (Oceania)]",
        ]
    },
    "roles": {
        "question": "What is your current role or position?",
        "columns": [
            "What is your current role or position in your organization?  [Business Analyst]",
            "What is your current role or position in your organization?  [Product Owner]",
            "What is your current role or position in your organization?  [Requirements Engineer]",
            "What is your current role or position in your organization?  [Software Architect]",
            "What is your current role or position in your organization?  [UI / UX Designer]",
            "What is your current role or position in your organization?  [Software Developer]",
            "What is your current role or position in your organization?  [Technical Leader]",
            "What is your current role or position in your organization?  [Project Manager]",
            "What is your current role or position in your organization?  [Other]",
        ]
    },
    "application_domains": {
        "question": "In which application domains have you worked?",
        "columns": APPLICATION_DOMAIN_COLS
    },
    "training_preferences": {
        "question": "Which training format would you prefer?",
        "columns": [
            "Which training format would you prefer? You can select up to three training formats.  [\"Classical Training\" (e.g., Classroom Training, Face-2-Face Training)]",
            "Which training format would you prefer? You can select up to three training formats.  [Community of practice]",
            "Which training format would you prefer? You can select up to three training formats.  [Newsletter]",
            "Which training format would you prefer? You can select up to three training formats.  [Workshops, tutorials and hands-on labs]",
            "Which training format would you prefer? You can select up to three training formats.  [Online courses and webinars]",
            "Which training format would you prefer? You can select up to three training formats.  [Mentoring programs]",
            "Which training format would you prefer? You can select up to three training formats.  [Blended learning programs]",
            "Which training format would you prefer? You can select up to three training formats.  [Case study analysis and group discussions]",
            "Which training format would you prefer? You can select up to three training formats.  [Conferences ]",
            "Which training format would you prefer? You can select up to three training formats.  [Hackathons]",
            "Which training format would you prefer? You can select up to three training formats.  [Other]",
        ]
    },
    "barriers": {
        "question": "What reasons prevent you from using GenAI in RE?",
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
        ]
    },
    "genai_re_disciplines": {
        "question": "For which RE disciplines did you use GenAI?",
        "columns": [
            "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Elicitation]",
            "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Analysis & Negotiation]",
            "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Specification / Requirements Modeling]",
            "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Validation / Quality Assurance]",
            "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Requirements Management]",
            "For which of the following RE-related disciplines did you use / apply GenAI?Please check all RE-related disciplines for which you have used GenAI and provide a short description of the particular tasks / goals that have been supported by AI (e.g., preparation of stakeholder interviews, analysis of elicited interview data, specification of user stories, etc.) [Other]",
        ]
    }
}

# Grouped task scales for RE phases (actual column names from CSV)
GROUPED_TASK_SCALES = {
    "Elicitation": {
        "question": "How useful/harmful is GenAI for Requirements Elicitation tasks?",
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
        "scales": [
            "Extremely useful",
            "Very useful",
            "Moderately useful",
            "Slightly useful",
            "Not useful at all",
            "I don't know",
            "Slightly harmful",
            "Moderately harmful",
            "Very harmful",
            "Extremely harmful",
            "Not harmful at all",
        ]
    },
    "Analysis & Negotiation": {
        "question": "How useful/harmful is GenAI for Requirements Analysis & Negotiation tasks?",
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
        "scales": [
            "Extremely useful",
            "Very useful",
            "Moderately useful",
            "Slightly useful",
            "Not useful at all",
            "I don't know",
            "Slightly harmful",
            "Moderately harmful",
            "Very harmful",
            "Extremely harmful",
            "Not harmful at all",
        ]
    },
    "Specification / Modeling": {
        "question": "How useful/harmful is GenAI for Requirements Specification / Modeling tasks?",
        "tasks": [
            "Creating document structures",
            "Drafting specifications",
            "Formulating requirements",
            "Creating use case descriptions",
            "Creating diagrams (e.g., UML models)",
            "Defining acceptance criteria",
        ],
        "scales": [
            "Extremely useful",
            "Very useful",
            "Moderately useful",
            "Slightly useful",
            "Not useful at all",
            "I don't know",
            "Slightly harmful",
            "Moderately harmful",
            "Very harmful",
            "Extremely harmful",
            "Not harmful at all",
        ]
    },
    "Validation / Quality Assurance": {
        "question": "How useful/harmful is GenAI for Requirements Validation / Quality Assurance tasks?",
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
        "scales": [
            "Extremely useful",
            "Very useful",
            "Moderately useful",
            "Slightly useful",
            "Not useful at all",
            "I don't know",
            "Slightly harmful",
            "Moderately harmful",
            "Very harmful",
            "Extremely harmful",
            "Not harmful at all",
        ]
    },
    "Management": {
        "question": "How useful/harmful is GenAI for Requirements Management tasks?",
        "tasks": [
            "Maintain requirements traceabilty",
            "Change management",
            "Configuration management (e.g., version control, document management)",
            "Requirements tracking and monitoring",
            "Requirements process assessment(e.g., auditing)",
        ],
        "scales": [
            "Extremely useful",
            "Very useful",
            "Moderately useful",
            "Slightly useful",
            "Not useful at all",
            "I don't know",
            "Slightly harmful",
            "Moderately harmful",
            "Very harmful",
            "Extremely harmful",
            "Not harmful at all",
        ]
    },
} 