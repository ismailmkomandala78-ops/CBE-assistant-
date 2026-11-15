import streamlit as st

st.set_page_config(page_title="CBE Assistant", page_icon="🎓")
st.title("🎓 CBE Assistant")
st.write("Niulize swali lolote la CBE - Accounting, IT, Marketing, Management!")

swali = st.text_input("Andika swali lako hapa:")

def jibu(swali):
    swali = swali.lower()
    if "habari" in swali or "mambo" in swali or "hello" in swali or "hi" in swali:
        return "Poa sana mkuu! Niko vizuri. Niulize swali la CBE."
    elif "jina" in swali or "nani wewe" in swali:
        return "Mimi ni CBE Assistant, nimeundwa kukusaidia kusoma CBE."
    elif "database" in swali or "hifadhidata" in swali:
        return "Database ni sehemu ya kuhifadhi data nyingi kwa mpangilio. Mfano: MySQL, Oracle."
    elif "faida" in swali or "profit" in swali:
        return "Faida = Mauzo - Gharama. Ukipata zaidi ya ulichotumia, umepata faida."
    elif "hasara" in swali or "loss" in swali:
        return "Hasara = Gharama - Mauzo. Ukipata chini ya ulichotumia, umepata hasara."
    elif "python" in swali:
        return "Python ni lugha ya programu rahisi kujifunza, inatumika kwa Web, AI na Data."
    elif "network" in swali or "mtandao" in swali:
        return "Network ni kuunganisha kompyuta nyingi ili zishirikiane data na vifaa kama printer."
    elif "accounting" in swali or "uhasibu" in swali:
        return "Accounting ni kuhesabu pesa za biashara: mapato, matumizi, faida na hasara."
    elif "marketing" in swali or "soko" in swali or "masoko" in swali:
        return "Marketing ni kutangaza na kuuza bidhaa kwa wateja. Mambo 4: Product, Price, Place, Promotion."
    elif "management" in swali or "uongozi" in swali:
        return "Management ni kupanga, kuongoza na kudhibiti kazi ili malengo ya biashara yafikiwe."
    elif "excel" in swali:
        return "Excel ni programu ya kuhesabu, kutengeneza majedwali na grafu. Inatumia formula kama =SUM()."
    elif "html" in swali:
        return "HTML ni lugha ya kutengeneza ukurasa wa tovuti. Inatumia tags kama <h1>, <p>."
    elif "css" in swali:
        return "CSS ni ya kupamba tovuti: rangi, ukubwa wa herufi na mpangilio."
    elif "javascript" in swali or "js" in swali:
        return "JavaScript ni lugha inayofanya tovuti iwe hai, mfano button ikibonyezwa inafanya kitu."
    elif "computer" in swali or "kompyuta" in swali:
        return "Kompyuta ni mashine inayopokea data, kuichakata na kutoa majibu. Sehemu zake: Hardware na Software."
    elif "hardware" in swali:
        return "Hardware ni sehemu zinazogusika za kompyuta: keyboard, mouse, monitor, CPU."
    elif "software" in swali:
        return "Software ni programu zinazoendesha kompyuta: mfano Windows, Word, WhatsApp."
    elif "cpu" in swali:
        return "CPU ni ubongo wa kompyuta. Inachakata maagizo yote."
    elif "ram" in swali:
        return "RAM ni kumbukumbu ya muda mfupi. Ukizima kompyuta, data yake inapotea."
    elif "rom" in swali:
        return "ROM ni kumbukumbu ya kudumu, haijafutika hata ukizima kompyuta."
    elif "internet" in swali:
        return "Internet ni mtandao mkubwa duniani unaounganisha kompyuta na simu nyingi."
    elif "email" in swali or "barua pepe" in swali:
        return "Email ni barua ya kielektroniki. Mfano: Gmail, Yahoo."
    elif "virus" in swali or "virusi" in swali:
        return "Virus ni programu mbaya inayoharibu kompyuta. Jilinde na Antivirus."
    elif "antivirus" in swali:
        return "Antivirus ni programu ya kulinda kompyuta dhidi ya virus."
    elif "mali" in swali or "asset" in swali:
        return "Mali (Asset) ni kitu biashara inachomiliki: pesa, gari, jengo, stock."
    elif "madeni" in swali or "liability" in swali:
        return "Madeni (Liability) ni pesa biashara inadaiwa na watu wengine."
    elif "mtaji" in swali or "capital" in swali:
        return "Mtaji (Capital) ni pesa mmiliki ameweka kwenye biashara."
    elif "mauzo" in swali or "sales" in swali:
        return "Mauzo (Sales) ni pesa unayopata baada ya kuuza bidhaa au huduma."
    elif "nunua" in swali or "purchase" in swali or "manunuzi" in swali:
        return "Manunuzi (Purchase) ni kununua bidhaa kwa ajili ya kuuza tena au kutumia."
    elif "bajeti" in swali or "budget" in swali:
        return "Bajeti ni mpango wa pesa: unapanga utatumia kiasi gani na utapata kiasi gani."
    elif "ushindani" in swali or "competition" in swali:
        return "Ushindani ni biashara zinazouza kitu kimoja kushindana kupata wateja."
    elif "mteja" in swali or "customer" in swali:
        return "Mteja ni mtu anayenunua bidhaa au huduma yako. Mteja ni mfalme!"
    elif "biashara" in swali:
        return "Biashara ni kununua na kuuza bidhaa au huduma ili kupata faida."
    elif "benki" in swali or "bank" in swali:
        return "Benki ni sehemu ya kuweka pesa, kukopa na kutuma pesa. Mfano: NMB, CRDB."
    elif "mkopo" in swali or "loan" in swali:
        return "Mkopo ni pesa unayokopa benki na unalipa baadaye pamoja na riba."
    elif "riba" in swali or "interest" in swali:
        return "Riba ni pesa ya ziada unayolipa ukikopa, au unayopata ukiweka pesa benki."
    elif "kodi" in swali or "tax" in swali:
        return "Kodi ni pesa unayolipa serikali kutokana na kipato au biashara yako."
    elif "stakabadhi" in swali or "receipt" in swali:
        return "Stakabadhi ni karatasi inayoonyesha umelipa / umenunua kitu."
    elif "ankara" in swali or "invoice" in swali:
        return "Invoice ni karatasi ya kudai malipo baada ya kuuza bidhaa."
    elif "hesabu" in swali or "equation" in swali:
        return "Mlinganyo wa Uhasibu: Mali = Madeni + Mtaji. Hii lazima iwe sawa kila wakati."
    elif "cbe" in swali:
        return "CBE ni Chuo cha Elimu ya Biashara (College of Business Education) - Dar es Salaam."
    elif "asante" in swali or "thanks" in swali:
        return "Karibu sana mkuu! Endelea kusoma, utafaulu!"
    elif "bye" in swali or "kwaheri" in swali:
        return "Kwaheri mkuu! Usisahau kurudi kusoma kesho."
    else:
        return "Samahani mkuu, sijajifunza hilo bado. Jaribu kuuliza kuhusu: faida, hasara, database, marketing, accounting, python, computer, biashara, benki, kodi."

if st.button("Uliza"):
    if swali:
        st.success(jibu(swali))
    else:
        st.warning("Andika swali kwanza mkuu!")
