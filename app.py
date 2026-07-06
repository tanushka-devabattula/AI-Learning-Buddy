import streamlit as st

from prompts import (
    explain_prompt,
    example_prompt,
    quiz_prompt,
    roadmap_prompt,
    interview_prompt,
    summary_prompt,
    flashcard_prompt,
    planner_prompt,
    resources_prompt,
    ask_anything_prompt,
    pdf_summary_prompt,
    pdf_quiz_prompt,
    pdf_flashcards_prompt,
    pdf_interview_prompt,
)

from utils import (
    generate_response,
    display_output,
    show_error,
    show_success,
)

from pdf_utils import (
    extract_text_from_pdf,
    clean_pdf_text,
    get_pdf_statistics,
)

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🤖",
    layout="wide",
)

# =====================================================
# Load CSS
# =====================================================

def load_css():
    with open("style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )

load_css()

# =====================================================
# Session State
# =====================================================

if "response" not in st.session_state:
    st.session_state.response = ""

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

# Interview Tab
if "interview_response" not in st.session_state:
    st.session_state.interview_response = ""

# Notes Tab
if "notes_response" not in st.session_state:
    st.session_state.notes_response = ""

# PDF Tab
if "pdf_response" not in st.session_state:
    st.session_state.pdf_response = ""

# Resources Tab
if "resource_response" not in st.session_state:
    st.session_state.resource_response = ""

# =====================================================
# Sidebar
# =====================================================

with st.sidebar:

    st.title("🤖 AI Learning Buddy")

    st.markdown("---")

    st.info(
        """
### Features

📘 Learn

💼 Interview Prep

📝 Notes

📄 PDF Tools

⚙️ Resources
"""
    )

    st.markdown("---")

    st.success("Powered by OpenRouter API")

# =====================================================
# Dashboard Title
# =====================================================

st.title("🤖 AI Learning Buddy")

st.caption(
    "Your AI-powered study assistant for learning, interview preparation, notes, PDFs, and resources."
)

st.divider()

# =====================================================
# Tabs
# =====================================================

learn_tab, interview_tab, notes_tab, pdf_tab, resource_tab = st.tabs(
    [
        "📘 Learn",
        "💼 Interview Prep",
        "📝 Notes",
        "📄 PDF Tools",
        "⚙️ Resources",
    ]
)
with learn_tab:

    st.subheader("📘 Learn")

    feature = st.selectbox(
        "Choose a learning tool",
        [
            "Explain Concept",
            "Real-Life Example",
            "Generate Quiz",
            "Learning Roadmap",
            "Ask Anything",
        ],
    )

    user_input = st.text_area(
        "Enter your topic or question",
        height=180,
        placeholder="Example: Binary Search, OOP, Operating System...",
    )

    if st.button(
        "🚀 Generate",
        use_container_width=True,
    ):

        if not user_input.strip():
            show_error("Please enter a topic.")
            st.stop()

        with st.spinner("Generating response..."):

            if feature == "Explain Concept":
                prompt = explain_prompt(user_input)

            elif feature == "Real-Life Example":
                prompt = example_prompt(user_input)

            elif feature == "Generate Quiz":
                prompt = quiz_prompt(user_input)

            elif feature == "Learning Roadmap":
                prompt = roadmap_prompt(user_input)

            else:
                prompt = ask_anything_prompt(user_input)

            result = generate_response(prompt)

            st.session_state.response = result

            show_success("Response generated successfully!")

    if st.session_state.response:

        st.markdown("---")

        display_output(
            feature,
            st.session_state.response,
        )
with interview_tab:

    st.subheader("💼 Interview Preparation")

    col1, col2 = st.columns(2)

    with col1:
        topic = st.text_input(
            "Topic",
            placeholder="Example: Java, DBMS, OOP...",
        )

    with col2:
        difficulty = st.selectbox(
            "Difficulty",
            [
                "Beginner",
                "Intermediate",
                "Advanced",
            ],
        )

    total_questions = st.slider(
        "Number of Questions",
        min_value=5,
        max_value=20,
        value=10,
    )

    if st.button(
        "🎯 Generate Interview Questions",
        use_container_width=True,
        key="interview_button",
    ):

        if not topic.strip():
            show_error("Please enter a topic.")
            st.stop()

        prompt = interview_prompt(
            f"""
Topic: {topic}

Difficulty: {difficulty}

Generate exactly {total_questions} interview questions with answers.
"""
        )

        with st.spinner("Preparing interview questions..."):

            result = generate_response(prompt)

            st.session_state.interview_response = result

            show_success("Interview Questions Generated!")

    if st.session_state.interview_response:

        st.markdown("---")

        display_output(
            "Interview Questions",
            st.session_state.interview_response,
        )
# =====================================================
# Notes Tab
# =====================================================

with notes_tab:

    st.subheader("📝 Notes")

    notes_feature = st.selectbox(
        "Choose a Notes Tool",
        [
            "Notes Summarizer",
            "Flashcards",
            "Study Planner"
        ],
        key="notes_feature"
    )

    notes_input = st.text_area(
        "Enter your notes or study topic",
        height=250,
        placeholder="Paste your notes or enter a topic...",
        key="notes_input"
    )

    if st.button(
        "📝 Generate",
        use_container_width=True,
        key="notes_button"
    ):

        if not notes_input.strip():
            show_error("Please enter some notes or a topic.")
            st.stop()

        with st.spinner("Generating..."):

            if notes_feature == "Notes Summarizer":
                prompt = summary_prompt(notes_input)

            elif notes_feature == "Flashcards":
                prompt = flashcard_prompt(notes_input)

            else:
                prompt = planner_prompt(notes_input)

            result = generate_response(prompt)

            st.session_state.notes_response = result

            show_success("Response generated successfully!")

    if st.session_state.notes_response:

        st.markdown("---")

        display_output(
            notes_feature,
            st.session_state.notes_response
        )
