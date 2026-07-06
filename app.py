import streamlit as st
import os
from openai import OpenAI

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="wide"
)

# ---------------- OPENROUTER ----------------
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# ---------------- HEADER ----------------
st.title("🎓 AI Learning Buddy")
st.caption("Your Personal AI Tutor for Learning, Practice & Interview Preparation")

st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📚 AI Learning Buddy")

st.sidebar.success("Features")

st.sidebar.markdown("""
✅ Explain Concept

✅ Real-Life Example

✅ Generate Quiz

✅ Learning Roadmap

🆕 Interview Questions

💬 Ask Anything
""")

st.sidebar.markdown("---")

st.sidebar.info("""
💡 Tip

Try topics like

• Python

• Java

• DBMS

• Operating Systems

• Cloud Computing

• Machine Learning
""")

# ---------------- INPUT ----------------

topic = st.text_input(
    "📘 Enter any topic",
    placeholder="Example: Python, Java, DBMS..."
)

activity = st.selectbox(
    "✨ Choose Learning Mode",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Learning Roadmap",
        "Interview Questions",
        "Ask Anything"
    ]
)

generate = st.button("🚀 Generate")

# ---------------- PROMPTS ----------------

if generate:

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if activity == "Explain Concept":

            prompt = f"""
Explain {topic} in beginner-friendly language.

Include:

• Definition

• Why it is important

• Key points

• Advantages

• Applications

Use simple English.
"""

        elif activity == "Real-Life Example":

            prompt = f"""
Give 5 simple real-life examples of {topic}.

Explain each example in 2-3 lines.
"""

        elif activity == "Generate Quiz":

            prompt = f"""
Create 10 multiple-choice questions on {topic}.

Each question must contain:

A)

B)

C)

D)

Mention the correct answer after every question.
"""

        elif activity == "Learning Roadmap":

            prompt = f"""
Create a complete roadmap for learning {topic}.

Format:

📘 Beginner

Topics

📙 Intermediate

Topics

📕 Advanced

Topics

Projects:

• Beginner Project

• Intermediate Project

• Advanced Project

Free Resources:

• Websites

• YouTube Channels

Estimated Time to Learn.
"""

        elif activity == "Interview Questions":

            prompt = f"""
Prepare interview questions on {topic}.

Include:

🟢 Beginner Questions (10)

🟡 Intermediate Questions (10)

🔴 Advanced Questions (10)

💻 Coding Questions (10 if applicable)

⭐ Interview Tips

📚 Best Resources to Prepare
"""

        else:

            prompt = topic

        with st.spinner("🤖 AI is thinking..."):

            try:

                response = client.chat.completions.create(
                    model="openrouter/auto",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                result = response.choices[0].message.content

                st.success("Response Generated Successfully!")

                st.markdown("---")

                st.subheader("🤖 AI Response")

                st.write(result)

                st.markdown("---")
                                # ---------- Download Response ----------

                st.download_button(
                    label="📥 Download Response",
                    data=result,
                    file_name=f"{topic.replace(' ', '_')}_AI_Response.txt",
                    mime="text/plain"
                )

                # ---------- Copy Hint ----------

                st.info("💡 Tip: You can also select the response above and copy it for your notes.")

            except Exception as e:

                st.error("❌ Something went wrong while generating the response.")
                st.error(str(e))

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    """
### 🚀 Available Features

- 📖 Explain Concept
- 🌍 Real-Life Example
- ❓ Generate Quiz
- 🗺️ Learning Roadmap
- 💼 Interview Questions
- 💬 Ask Anything

---
"""
)

st.caption("🎓 AI Learning Buddy | Built with ❤️ using Python, Streamlit & OpenRouter")

st.sidebar.markdown("---")

st.sidebar.markdown("### 📌 Upcoming Features")

st.sidebar.markdown("""
- 📝 Notes Summarizer
- 🧠 Flashcards Generator
- 📅 Study Planner
- 📄 PDF Upload & AI Chat
- 🎯 Daily Challenge
- 🌙 Enhanced UI
""")
