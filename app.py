import streamlit as st

st.set_page_config(page_title="CBE Smart Assistant", page_icon="🎓")
st.title("🎓 CBE Smart Assistant")
st.write("Uliza swali kuhusu CBE. Mfano: Database, Faida, Python, Marketing")

def jibu(swali):
    swali = swali.lower()
    if "habari" in swali or "mambo" in swali or "hello" in swali:
        return "Poa sana mkuu! Niko vizuri. Uliza chochote kuhusu CBE."
    elif "database" in swali:
        return "Database ni sehemu ya kuhifadhi data. Mfano wa CBE: kuhifadhi majina na alama."
    elif "faida" in swali or "profit" in swali:
        return "Faida = Mauzo - Gharama. Ulinunua 5000, ukauza 7000 = Faida 2000"
    elif "hasara" in swali or "loss" in swali:
        return "Hasara = Gharama - Mauzo. Ulinunua 7000, ukauza 5000 = Hasara 2000."
    elif "python" in swali:
        return "Python ni lugha ya programu. Rahisi kujifunza, inatumika kutengeneza App kama hii."
    elif "network" in swali:
        return "Network ni kuunganisha kompyuta. WiFi ya CBE inaunganisha simu na kompyuta."
    elif "accounting" in swali or "uhasibu" in swali:
        return "Accounting ni kuhesabu pesa za biashara: Mauzo, Gharama, Faida."
    elif "marketing" in swali or "soko" in swali:
        return "Marketing ni kutangaza na kuuza bidhaa. Mfano: Kuweka matangazo Instagram ili watu waje kununua."
    elif "management" in swali or "uongozi" in swali:
        return "Management ni kupanga, kuongoza na kudhibiti watu na rasilimali ili biashara ifanikiwe."
    elif "economics" in swali or "uchumi" in swali:
        return "Economics ni kusoma jinsi watu wanavyotumia pesa na rasilimali chache kukidhi mahitaji mengi."
    elif "excel" in swali:
        return "Excel ni programu ya kuhesabu. Unatumia =SUM(A1:A5) kujumlisha, na =AVERAGE kupata wastani."
    elif "internet" in swali:
        return "Internet ni mtandao mkubwa unaounganisha dunia nzima."
    elif "cbe" in swali:
        return "CBE ni College of Business Education. Chuo bora Tanzania kwa Biashara na IT!"
    elif "asante" in swali or "thank" in swali:
        return "Karibu sana mkuu! Soma vizuri, utafaulu. 💪"
    else:
        return "Swali zuri! Jaribu: Database, Faida, Python, Network, Accounting, Marketing, Management, Economics, Excel, CBE"

swali = st.text_input("✍️ Swali lako:")
if st.button("Uliza"):
    if swali:
        st.success("🤖: " + jibu(swali))
    else:
        st.warning("Tafadhali andika swali kwanza!")
    
