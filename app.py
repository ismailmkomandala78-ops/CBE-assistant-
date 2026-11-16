import streamlit as st
from google import genai

st.set_page_config(page_title="CBE Assistant AI", page_icon="🎓")
st.title("🎓 CBE Assistant - AI")
st.write("Sasa najibu swali LOLOTE kama ChatGPT!")

# --- WEKA KEY HAPA ---
st.sidebar.header("🔑 Setting")
api_key = st.sidebar.text_input("Weka Gemini API Key yako hapa:", type="password", help="Copy kutoka Google AI Studio")
st.sidebar.caption("Key yako haionekani na mtu, inakaa kwenye simu yako tu.")

if not api_key:
    st.warning("👈 Weka API Key yako hapo kushoto (sidebar) ili niweze kujibu.")
    st.info("Huna Key? Nenda Google AI Studio > Copy key > Rudi hapa u-paste.")
    st.stop()

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
            try:
                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=f"Wewe ni mwalimu wa CBE Tanzania. Jibu kwa Kiswahili rahisi na mifano ya Tanzania. Swali: {swali}"
                )
                jibu = response.text
                st.write(jibu)
                st.session_state.chat.append({"role": "assistant", "text": jibu})
            except Exception as e:
                st.error(f"Samahani, kuna tatizo: {e}. Hakikisha Key ni sahihi.")
        
