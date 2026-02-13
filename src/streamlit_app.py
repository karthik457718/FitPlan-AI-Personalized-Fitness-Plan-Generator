import streamlit as st
import time

st.set_page_config(page_title="FitPlan AI Elite", page_icon="💎", layout="wide")

st.markdown("""
<style>

/* ===== GOOGLE FONT ===== */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

/* ===== CINEMATIC GYM BACKGROUND ===== */
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(rgba(10,10,20,0.75), rgba(10,10,20,0.75)),
        url("https://images.unsplash.com/photo-1599058917765-a780eda07a3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* ===== FLOATING PARTICLES ===== */
body::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,0,200,0.12) 2px, transparent 2px);
    background-size: 70px 70px;
    animation: moveParticles 80s linear infinite;
    z-index: 0;
}

@keyframes moveParticles {
    from { transform: translate(0,0); }
    to { transform: translate(-400px,-400px); }
}

/* ===== CENTER LAYOUT ===== */
.block-container {
    max-width: 950px;
    margin: auto;
    padding-top: 70px;
    position: relative;
    z-index: 1;
}

/* ===== HERO TITLE ===== */
h1 {
    text-align: center;
    font-size: 52px !important;
    font-weight: 700 !important;
    color: white !important;
}

h2, h3, h4, p, label {
    color: white !important;
}

/* ===== GLOW HERO BAR (3rd image style) ===== */
.glow-bar {
    height: 80px;
    border-radius: 50px;
    margin: 40px auto;
    position: relative;
    background: rgba(255,255,255,0.05);
    width: 80%;
}

.glow-bar::before {
    content: "";
    position: absolute;
    inset: -3px;
    border-radius: 50px;
    padding: 3px;
    background: linear-gradient(90deg, #ff00cc, #7928ca, #00f0ff);
    -webkit-mask:
        linear-gradient(#000 0 0) content-box,
        linear-gradient(#000 0 0);
    -webkit-mask-composite: xor;
            mask-composite: exclude;
    animation: glowMove 4s linear infinite;
}

@keyframes glowMove {
    0% { background: linear-gradient(90deg, #ff00cc, #7928ca, #00f0ff); }
    50% { background: linear-gradient(90deg, #00f0ff, #ff00cc, #7928ca); }
    100% { background: linear-gradient(90deg, #ff00cc, #7928ca, #00f0ff); }
}

/* ===== GLASS CARD ===== */
.glass {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(35px);
    border-radius: 30px;
    padding: 45px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 0 80px rgba(255,0,200,0.25);
    margin-bottom: 35px;
}

/* ===== GLASS INPUTS ===== */
.stTextInput input,
.stNumberInput input,
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.1) !important;
    border-radius: 30px !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    color: white !important;
    padding: 16px !important;
    backdrop-filter: blur(20px);
}

/* Remove number input arrow background */
.stNumberInput button {
    background: transparent !important;
    color: white !important;
}

/* ===== GLASS BUTTON ===== */
.stButton > button {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(20px);
    border-radius: 40px;
    padding: 14px 45px;
    border: 1px solid rgba(255,255,255,0.4);
    color: white;
    font-weight: 600;
    transition: 0.3s ease;
}

.stButton > button:hover {
    background: rgba(255,255,255,0.2);
    box-shadow: 0 0 40px rgba(255,0,200,0.5);
    transform: translateY(-3px);
}

</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("<h1>💎 FitPlan AI Elite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Train Smart. Perform Elite.</p>", unsafe_allow_html=True)
st.markdown('<div class="glow-bar"></div>', unsafe_allow_html=True)

# FORM CARD
st.markdown('<div class="glass">', unsafe_allow_html=True)

name = st.text_input("Full Name")
height_cm = st.number_input("Height (cm)", min_value=0.0)
weight_kg = st.number_input("Weight (kg)", min_value=0.0)

goal = st.selectbox("Goal",
    ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
)

level = st.selectbox("Level",
    ["Beginner", "Intermediate", "Advanced"]
)

equipment = st.multiselect("Equipment",
    ["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment",
     "Bench", "Treadmill", "Cycle", "Pullup Bar"]
)

generate = st.button("Generate Elite Plan 🚀")

st.markdown('</div>', unsafe_allow_html=True)

# BMI Logic
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# RESULTS
if generate:
    if name.strip() == "" or height_cm <= 0 or weight_kg <= 0:
        st.error("Please complete all fields properly.")
    else:
        bmi = calculate_bmi(height_cm, weight_kg)
        category = bmi_category(bmi)

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader(name)
        st.markdown(f"## BMI: {bmi}")
        st.markdown(f"### Category: {category}")

        progress = min(bmi / 40, 1.0)
        bar = st.progress(0)
        for i in range(int(progress * 100)):
            time.sleep(0.01)
            bar.progress(i + 1)

        st.markdown('</div>', unsafe_allow_html=True)