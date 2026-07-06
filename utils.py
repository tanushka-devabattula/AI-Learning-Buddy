import requests
import streamlit as st


def call_openrouter(prompt):
    """
    Sends a prompt to OpenRouter API and returns the generated response.
    """

    api_key = st.secrets.get("OPENROUTER_API_KEY")

    if not api_key:
        return "❌ OpenRouter API Key not found."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "AI Learning Buddy",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "openai/gpt-4.1-mini",
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "temperature": 0.7,
        "max_tokens": 1200,
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=90,
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "⏳ Request timed out. Please try again."

    except requests.exceptions.ConnectionError:
        return "🌐 Internet connection error."

    except Exception as e:
        return f"❌ {e}"


def generate_response(prompt):
    """
    Wrapper function for future extensibility.
    """
    return call_openrouter(prompt)


def download_text(text, filename="output.txt"):
    """
    Creates a download button.
    """

    st.download_button(
        label="📥 Download Result",
        data=text,
        file_name=filename,
        mime="text/plain",
        use_container_width=True,
    )


def copy_button():
    """
    Displays a small tip for copying.
    """

    st.info("💡 Tip: Select the response and press Ctrl+C to copy.")


def display_output(title, content):
    """
    Displays AI output in a clean, professional container.
    """

    with st.container():

        st.subheader(title)

        st.markdown(content)

        st.download_button(
            label="📥 Download Result",
            data=content,
            file_name="result.txt",
            mime="text/plain",
            use_container_width=True,
        )

        st.info("💡 Tip: Select the response and press Ctrl+C to copy.")


def show_success(message):
    st.success(message)


def show_error(message):
    st.error(message)


def show_warning(message):
    st.warning(message)


def show_info(message):
    st.info(message)
