import streamlit as st

from prompts import (
    explain_prompt,
    example_prompt,
    quiz_prompt,
    roadmap_prompt,
    interview_prompt,
    summary_prompt
)

from utils import generate_response


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="wide"
)


# ---------------- HEADER ----------------

st.title("🎓 AI Learning Buddy")
st.subheader("Learn Anything with AI")

st.markdown("---")


# ---------------- SIDEBAR ----------------

st.sidebar.title("📚 AI Learning Buddy")

st.sidebar.info(
    """
Features

📖 Explain Concept

🌍 Real-Life Example

❓ Generate Quiz

🗺️ Learning Roadmap

💼 Interview Questions

📝 Notes Summarizer

💬 Ask Anything
"""
)

st.sidebar.markdown("---")

st.sidebar.success("Made with ❤️ using Streamlit + OpenRouter")


# ---------------- INPUT ----------------

activity = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Learning Roadmap",
        "Interview Questions",
        "Notes Summarizer",
        "Ask Anything"
    ]
)


# ---------------- INPUT BOX ----------------

if activity == "Notes Summarizer":

    user_input = st.text_area(
        "Paste your notes here",
        height=250
    )

else:

    user_input = st.text_input(
        "Enter a topic",
        placeholder="Example: Python, DBMS, AI..."
    )


# ---------------- BUTTON ----------------

if st.button("🚀 Generate"):

    if user_input.strip() == "":

        st.warning("Please enter some text.")

    else:

        if activity == "Explain Concept":

            prompt = explain_prompt(user_input)

        elif activity == "Real-Life Example":

            prompt = example_prompt(user_input)

        elif activity == "Generate Quiz":

            prompt = quiz_prompt(user_input)

        elif activity == "Learning Roadmap":

            prompt = roadmap_prompt(user_input)

        elif activity == "Interview Questions":

            prompt = interview_prompt(user_input)

        elif activity == "Notes Summarizer":

            prompt = summary_prompt(user_input)

        else:

            prompt = user_input

        with st.spinner("Generating response..."):

            try:

                result = generate_response(prompt)

                st.success("Response Generated Successfully!")

                st.markdown("## 🤖 AI Response")

                st.write(result)

                st.download_button(
                    "📥 Download Response",
                    result,
                    file_name="AI_Response.txt"
                )

            except Exception as e:

                st.error(str(e))


st.markdown("---")

st.caption("© 2026 AI Learning Buddy")
