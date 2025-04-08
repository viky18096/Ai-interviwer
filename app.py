import streamlit as st
import speech_recognition as sr
from utils.ai_core import generate_question_response, extract_claims
from utils.claim_verifier import mock_verify_claim

st.set_page_config(page_title="🧠 Political Interview AI", layout="centered")

st.title("🎙️ Voice-Based Political Interviewer")
st.markdown("Powered by Phi-4 + Real-Time Claim Checker")

if 'q_index' not in st.session_state:
    st.session_state.q_index = 0

with open("questions.txt", "r", encoding="utf-8") as f:
    questions = [q.strip() for q in f.readlines() if q.strip()]

if st.button("🎤 Start / Next Question"):
    if st.session_state.q_index < len(questions):
        q = questions[st.session_state.q_index]
        st.write(f"**🧠 AI Asks:** {q}")

        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("Listening for politician's response...")
            audio = recognizer.listen(source, timeout=10)
            try:
                response = recognizer.recognize_google(audio)
                st.success(f"🗣️ You said: {response}")
                
                claims = extract_claims(response).split("\n")
                st.markdown("### 🔍 Extracted Claims and Fact Checks")
                for claim in claims:
                    result = mock_verify_claim(claim)
                    st.write(f"- **Claim:** {claim.strip()} \n➡️ **Status:** {result}")

                follow_up = generate_question_response(q, response)
                st.markdown("### 🤖 AI Follow-Up")
                st.write(follow_up)
                
                st.session_state.q_index += 1
            except:
                st.error("Could not recognize the response.")
    else:
        st.balloons()
        st.success("✅ Interview session complete.")
