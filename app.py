
import streamlit as st
from groq import Groq
import os

st.set_page_config(
    page_title="RIO - AI Biology Tutor",
    page_icon="🧬",
    layout="centered"
)

st.title("🧬 RIO - AI Biology Tutor")
st.caption("Your personal AI Biology teacher | Class 10")

st.write(
    "Enter any Biology topic and RIO will explain it "
    "with definitions, examples, diagrams and practice questions."
)

language = st.selectbox(
    "Choose your answer language",
    ["English + Roman Urdu", "English", "Roman Urdu"]
)

topic = st.text_input(
    "Enter your Biology topic",
    placeholder="e.g. Introduction to Biology"
)

if st.button("Generate Explanation", type="primary"):
    if not topic.strip():
        st.warning("Please enter a Biology topic.")
    else:
        try:
            api_key = st.secrets["GROQ_API_KEY"]
            client = Groq(api_key=api_key)

            prompt = f"""
You are RIO, a friendly Biology tutor for Class 10 students.

Explain the topic: {topic}

Answer language: {language}

Include:
1. Topic name
2. Clear definition
3. Detailed explanation
4. Important points
5. Daily-life examples
6. A simple text-based labeled diagram
7. Five practice questions with answers

Use correct scientific information and student-friendly language.
If Roman Urdu is selected, explain in Roman Urdu.
If English + Roman Urdu is selected, provide both.
"""

            with st.spinner("RIO is preparing your lesson..."):
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are RIO, a helpful Class 10 Biology tutor."
                        },
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.4
                )

            st.markdown(f"## 📘 Topic: {topic}")
            st.markdown(response.choices[0].message.content)

        except Exception as e:
            st.error(
                "RIO could not generate the lesson. "
                "Please check your Groq API key and app settings."
            )
