import streamlit as st
from google import genai

st.set_page_config(page_title="CBE Assistant - AI")
st.title("🎓 CBE Assistant - AI")
st.write("Sasa najibu swali LOLOTE kama ChatGPT!")

# --- WEKA KEY HAPA ---
st.sidebar.header("🔑 Setting")
api_key = st.sidebar.text_input("Weka API Key yako hapa", type="password")
st.sidebar.caption("Key yako haionekani kwa wengine")

if not api_key:
    st.warning("👉 Weka API Key yako hapo kando")
    st.info("Huna Key? Nenda Google AI Studio")
    st.stop()

client = genai.Client(api_key=api_key)

MODELS = [
    "gemini-3.8-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-2.5-flash-lite",
]

# --- CHAT ---
if "chat" not in st.session_state:
    st.session_state.chat = []

for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.write(msg["text"])

swali = st.chat_input("Andika swali lolote la CBE hapa...")

if swali:
    st.session_state.chat.append({"role": "user", "text": swali})
    with st.chat_message("user"):
        st.write(swali)

    with st.chat_message("assistant"):
        with st.spinner("Nafikiria..."):
            jibu = None
            for model_name in MODELS:
                try:
                    response = client.models.generate_content(
                        model=model_name,
                        contents=f"Wewe ni mwalimu wa CBE. Jibu kwa Kiswahili rahisi: {swali}"
                    )
                    jibu = response.text
                    break
                except Exception:
                    continue
            
            if jibu:
                st.write(jibu)
                st.session_state.chat.append({"role": "assistant", "text": jibu})
            else:
                st.warning("Pole Mkuu, Google imezidiwa sana sasa hivi. Subiri sekunde 20 kisha uliza tena.")
