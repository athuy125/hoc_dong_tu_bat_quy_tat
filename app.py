import streamlit as st
import random
import pandas as pd

# ========================
# DỮ LIỆU
# ========================

# Đuôi từ loại (cập nhật theo yêu cầu)
suffixes = {
    "noun": ["ment","ance","ion","ation","age","al","ing","er","or","ist","ress","ant","ess","ee","ledge","ar","ence","ness","ity","acy","dom","ism","th","hood","ship"],
    "verb": ["en","ise","ize","ate","fy"],
    "adjective": ["ly","ful","less","ic","able","ous","some","al","ing","ed","ern","y","ible","ent","ive","like","ish","ary"],
    "adverb": ["ly"]
}

# Động từ bất quy tắc (cập nhật theo yêu cầu)
irregular_verbs = [
    {"base": "awake", "past": "awoke", "pp": "awaken"},
    {"base": "be", "past": "was/were", "pp": "been"},
    {"base": "beat", "past": "beat", "pp": "beaten"},
    {"base": "begin", "past": "began", "pp": "begun"},
    {"base": "bite", "past": "bit", "pp": "bitten"},
    {"base": "blow", "past": "blew", "pp": "blown"},
    {"base": "break", "past": "broke", "pp": "broken"},
    {"base": "bring", "past": "brought", "pp": "brought"},
    {"base": "build", "past": "built", "pp": "built"},
    {"base": "buy", "past": "bought", "pp": "bought"},
    {"base": "catch", "past": "caught", "pp": "caught"},
    {"base": "choose", "past": "chose", "pp": "chosen"},
    {"base": "come", "past": "came", "pp": "come"},
    {"base": "cost", "past": "cost", "pp": "cost"},
    {"base": "cut", "past": "cut", "pp": "cut"},
    {"base": "do", "past": "did", "pp": "done"},
    {"base": "deal", "past": "dealt", "pp": "dealt"},
    {"base": "dig", "past": "dug", "pp": "dug"},
    {"base": "draw", "past": "drew", "pp": "drawn"},
    {"base": "dream", "past": "dreamt", "pp": "dreamt"},
    {"base": "drink", "past": "drank", "pp": "drunk"},
    {"base": "drive", "past": "drove", "pp": "driven"},
    {"base": "eat", "past": "ate", "pp": "eaten"},
    {"base": "fall", "past": "fell", "pp": "fallen"},
    {"base": "feed", "past": "fed", "pp": "fed"},
    {"base": "feel", "past": "felt", "pp": "felt"},
    {"base": "fight", "past": "fought", "pp": "fought"},
    {"base": "find", "past": "found", "pp": "found"},
    {"base": "fly", "past": "flew", "pp": "flown"},
    {"base": "forget", "past": "forgot", "pp": "forgotten"},
    {"base": "forgive", "past": "forgave", "pp": "forgiven"},
    {"base": "freeze", "past": "froze", "pp": "frozen"},
    {"base": "get", "past": "got", "pp": "gotten"},
    {"base": "give", "past": "gave", "pp": "given"},
    {"base": "go", "past": "went", "pp": "gone"},
    {"base": "grow", "past": "grew", "pp": "grown"},
    {"base": "hang", "past": "hung", "pp": "hung"},
    {"base": "have", "past": "had", "pp": "had"},
    {"base": "hear", "past": "heard", "pp": "heard"},
    {"base": "hide", "past": "hid", "pp": "hidden"},
    {"base": "hit", "past": "hit", "pp": "hit"},
    {"base": "hold", "past": "held", "pp": "held"},
    {"base": "hurt", "past": "hurt", "pp": "hurt"},
    {"base": "keep", "past": "kept", "pp": "kept"},
    {"base": "know", "past": "knew", "pp": "known"},
    {"base": "lay", "past": "laid", "pp": "laid"},
    {"base": "lead", "past": "led", "pp": "led"},
    {"base": "leave", "past": "left", "pp": "left"},
    {"base": "lend", "past": "lent", "pp": "lent"},
    {"base": "lie", "past": "lay", "pp": "lain"},
    {"base": "lose", "past": "lost", "pp": "lost"},
    {"base": "make", "past": "made", "pp": "made"},
    {"base": "mean", "past": "meant", "pp": "meant"},
    {"base": "meet", "past": "met", "pp": "met"},
    {"base": "pay", "past": "paid", "pp": "paid"},
    {"base": "put", "past": "put", "pp": "put"},
    {"base": "quit", "past": "quit", "pp": "quit"},
    {"base": "read", "past": "read", "pp": "read"},
    {"base": "ride", "past": "rode", "pp": "ridden"},
    {"base": "ring", "past": "rang", "pp": "rung"},
    {"base": "rise", "past": "rose", "pp": "risen"},
    {"base": "run", "past": "ran", "pp": "run"},
    {"base": "say", "past": "said", "pp": "said"},
    {"base": "see", "past": "saw", "pp": "seen"},
    {"base": "sell", "past": "sold", "pp": "sold"},
    {"base": "send", "past": "sent", "pp": "sent"},
    {"base": "set", "past": "set", "pp": "set"},
    {"base": "sew", "past": "sewed", "pp": "sewn"},
    {"base": "shake", "past": "shook", "pp": "shaken"},
    {"base": "shine", "past": "shone", "pp": "shone"},
    {"base": "shoot", "past": "shot", "pp": "shot"},
    {"base": "show", "past": "showed", "pp": "shown"},
    {"base": "shut", "past": "shut", "pp": "shut"},
    {"base": "sing", "past": "sang", "pp": "sung"},
    {"base": "sink", "past": "sank", "pp": "sunk"},
    {"base": "sit", "past": "sat", "pp": "sat"},
    {"base": "sleep", "past": "slept", "pp": "slept"},
    {"base": "slide", "past": "slid", "pp": "slid"},
    {"base": "speak", "past": "spoke", "pp": "spoken"},
    {"base": "spend", "past": "spent", "pp": "spent"},
    {"base": "spread", "past": "spread", "pp": "spread"},
    {"base": "stand", "past": "stood", "pp": "stood"},
    {"base": "steal", "past": "stole", "pp": "stolen"},
    {"base": "stick", "past": "stuck", "pp": "stuck"},
    {"base": "strike", "past": "struck", "pp": "struck"},
    {"base": "swear", "past": "swore", "pp": "sworn"},
    {"base": "sweep", "past": "swept", "pp": "swept"},
    {"base": "swim", "past": "swam", "pp": "swum"},
    {"base": "swell", "past": "swelled", "pp": "swollen"},
    {"base": "swing", "past": "swung", "pp": "swung"},
    {"base": "take", "past": "took", "pp": "taken"},
    {"base": "teach", "past": "taught", "pp": "taught"},
    {"base": "tear", "past": "tore", "pp": "torn"},
    {"base": "tell", "past": "told", "pp": "told"},
    {"base": "think", "past": "thought", "pp": "thought"},
    {"base": "wear", "past": "wore", "pp": "worn"},
    {"base": "weep", "past": "wept", "pp": "wept"},
    {"base": "win", "past": "won", "pp": "won"},
    {"base": "write", "past": "wrote", "pp": "written"},
]

# ========================
# TRẠNG THÁI
# ========================
if "mode" not in st.session_state:
    st.session_state.mode = None
if "unused_suffixes" not in st.session_state:
    st.session_state.unused_suffixes = [(cat, suf) for cat, sufs in suffixes.items() for suf in sufs]
if "current_suffix" not in st.session_state:
    st.session_state.current_suffix = None
if "unused_verbs" not in st.session_state:
    st.session_state.unused_verbs = irregular_verbs.copy()
if "current_verb" not in st.session_state:
    st.session_state.current_verb = None
if "verb_started" not in st.session_state:
    st.session_state.verb_started = False

st.title("📚 Web học từ vựng tiếng Anh")

if st.session_state.mode is None:
    st.subheader("Chọn chế độ học:")
    if st.button("📖 Học đuôi từ loại"):
        st.session_state.mode = "suffix"
        st.rerun()
    if st.button("🔤 Học động từ bất quy tắc"):
        st.session_state.mode = "verb"
        st.rerun()

elif st.session_state.mode == "suffix":
    if not st.session_state.unused_suffixes:
        st.session_state.unused_suffixes = [(cat, suf) for cat, sufs in suffixes.items() for suf in sufs]
        st.info("🔄 Hoàn thành một vòng học đuôi từ loại! Bắt đầu lại.")

    if st.session_state.current_suffix is None:
        st.session_state.current_suffix = random.choice(st.session_state.unused_suffixes)
        st.session_state.unused_suffixes.remove(st.session_state.current_suffix)

    category, suffix = st.session_state.current_suffix
    st.write(f"Đuôi cần đoán: **_{suffix}**")
    user_type = st.text_input("Đây là loại từ gì?")

    if st.button("Kiểm tra"):
        if user_type.strip().lower() in [category.lower(), 
                                         "noun" if category=="noun" else "",
                                         "verb" if category=="verb" else "",
                                         "adjective" if category=="adjective" else "",
                                         "adverb" if category=="adverb" else "",
                                         "danh từ" if category=="noun" else "",
                                         "động từ" if category=="verb" else "",
                                         "tính từ" if category=="adjective" else "",
                                         "trạng từ" if category=="adverb" else ""]:
            st.success("✅ Chính xác!")
        else:
            st.error(f"❌ Sai! Đúng là: {category}")

    if st.button("Từ tiếp theo"):
        st.session_state.current_suffix = None
        st.rerun()

    if st.button("🔙 Quay lại menu"):
        st.session_state.mode = None
        st.rerun()


elif st.session_state.mode == "verb":

    # Nếu chưa bắt đầu -> hiện bảng ôn tập
    if not st.session_state.verb_started:
        st.subheader("📋 Bảng động từ bất quy tắc để ôn tập:")
        df = pd.DataFrame(irregular_verbs)
        st.table(df)

        if st.button("▶️ Bắt đầu học"):
            st.session_state.verb_started = True
            st.session_state.verb_index = 0   # bắt đầu từ từ đầu tiên
            st.rerun()

        if st.button("🔙 Quay lại menu"):
            st.session_state.mode = None
            st.rerun()

    else:
        # Nếu chưa có index thì gán bằng 0
        if "verb_index" not in st.session_state:
            st.session_state.verb_index = 0

        # Lấy động từ hiện tại theo thứ tự
        current_verb = irregular_verbs[st.session_state.verb_index]

        base = current_verb["base"]
        st.write(f"Động từ: **{base}**")

        user_past = st.text_input("Cột 2 (Quá khứ đơn):", key="past_input")
        user_pp = st.text_input("Cột 3 (Quá khứ phân từ):", key="pp_input")

        if st.button("Kiểm tra"):
            correct_past = current_verb["past"].lower()
            correct_pp = current_verb["pp"].lower()
            if user_past.strip().lower() == correct_past and user_pp.strip().lower() == correct_pp:
                st.success("✅ Chính xác!")
            else:
                st.error(f"❌ Sai! Đúng là: {current_verb['past']} - {current_verb['pp']}")

        if st.button("Hiện đáp án"):
            st.info(f"➡️ {base} - {current_verb['past']} - {current_verb['pp']}")

        if st.button("Từ tiếp theo"):
            st.session_state.verb_index += 1
            if st.session_state.verb_index >= len(irregular_verbs):  # hết danh sách thì quay lại từ đầu
                st.session_state.verb_index = 0
                st.info("🔄 Hoàn thành một vòng học động từ bất quy tắc! Bắt đầu lại từ đầu.")
            st.rerun()

        if st.button("🔙 Quay lại menu"):
            st.session_state.mode = None
            st.session_state.verb_started = False
            st.session_state.verb_index = 0
            st.rerun()

