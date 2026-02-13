import streamlit as st
import time

st.set_page_config(page_title="FitPlan AI Ultra", page_icon="💎", layout="wide")

st.markdown("""
<style>

/* ===== FUTURISTIC FONT ===== */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
}

/* ===== CINEMATIC BACKGROUND ===== */
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(rgba(5,5,20,0.8), rgba(5,5,20,0.8)),
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
    background-size: 60px 60px;
    animation: moveParticles 100s linear infinite;
    z-index: 0;
}

@keyframes moveParticles {
    from { transform: translate(0,0); }
    to { transform: translate(-500px,-500px); }
}

/* ===== CENTER LAYOUT ===== */
.block-container {
    max-width: 850px;
    margin: auto;
    padding-top: 70px;
    position: relative;
    z-index: 1;
}

/* ===== HERO ===== */
h1 {
    text-align: center;
    font-size: 48px !important;
    font-weight: 800 !important;
    color: white !important;
    letter-spacing: 2px;
}

h2, h3, h4, p, label {
    color: white !important;
}

/* ===== GLASS INPUT STYLE ===== */
div[data-baseweb="input"] {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 40px !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    backdrop-filter: blur(20px);
    transition: 0.3s ease;
}

/* Glow on focus */
div[data-baseweb="input"]:focus-within {
    box-shadow: 0 0 20px rgba(255,0,200,0.6);
    border: 1px solid rgba(255,0,200,0.8) !important;
}

/* Remove white inner layer */
div[data-baseweb="input"] > div {
    background: transparent !important;
}

/* Transparent input */
div[data-baseweb="input"] input {
    background: transparent !important;
    color: white !important;
    border: none !important;
    padding: 16px !important;
}

/* Select styling */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 40px !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    backdrop-filter: blur(20px);
    color: white !important;
}

/* ===== FUTURISTIC BUTTON ===== */
.stButton > button {
    position: relative;
    background: rgba(255,255,255,0.08);
    border-radius: 50px;
    padding: 14px 50px;
    border: 2px solid rgba(255,255,255,0.4);
    color: white;
    font-weight: 600;
    overflow: hidden;
    transition: 0.3s ease;
}

/* Animated Neon Border */
.stButton > button:hover {
    border: 2px solid transparent;
    transform: translateY(-4px);
}

/* Gradient Border Animation */
.stButton > button:hover::before {
    content: "";
    position: absolute;
    inset: -3px;
    border-radius: 50px;
    padding: 3px;
    background: linear-gradient(90deg, #ff00cc, #7928ca, #00f0ff);
    background-size: 300% 300%;
    animation: gradientMove 4s linear infinite;
    -webkit-mask:
        linear-gradient(#000 0 0) content-box,
        linear-gradient(#000 0 0);
    -webkit-mask-composite: xor;
            mask-composite: exclude;
}

/* Gradient animation */
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Glow effect */
.stButton > button:hover {
    box-shadow: 0 0 25px rgba(255,0,200,0.7),
                0 0 50px rgba(120,0,255,0.5);
}

/* Ripple click effect */
.stButton > button:active {
    transform: scale(0.96);
}

</style>
""", unsafe_allow_html=True)

# ===== HERO =====
st.markdown("<h1>💎 FITPLAN AI ULTRA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>FUTURISTIC FITNESS INTELLIGENCE</p>", unsafe_allow_html=True)

# ===== FORM =====
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

generate = st.button("Generate Ultra Plan 🚀")

# ===== BMI =====
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

# ===== WORKOUT =====
def generate_workout(goal, level):
    plans = {
        "Weight Loss": ["HIIT Sprint", "Burpees", "Mountain Climbers"],
        "Build Muscle": ["Bench Press", "Squats", "Pullups"],
        "Strength Gain": ["Deadlifts", "Heavy Pullups"],
        "Abs Building": ["Planks", "Leg Raises"],
        "Flexible": ["Yoga Flow", "Mobility Training"]
    }
    workout = plans.get(goal, [])
    if level == "Intermediate":
        workout = [w + " 🔥" for w in workout]
    elif level == "Advanced":
        workout = [w + " 💎 ELITE" for w in workout]
    return workout

# ===== RESULTS =====
if generate:
    if name.strip() == "" or height_cm <= 0 or weight_kg <= 0:
        st.error("Please complete all fields properly.")
    else:
        bmi = calculate_bmi(height_cm, weight_kg)
        category = bmi_category(bmi)

        st.subheader(f"👤 {name}")
        st.markdown(f"## BMI: {bmi}")
        st.markdown(f"### Category: {category}")

        progress = min(bmi / 40, 1.0)
        bar = st.progress(0)
        for i in range(int(progress * 100)):
            time.sleep(0.01)
            bar.progress(i + 1)

        st.markdown("---")
        st.subheader("🏋️ ULTRA WORKOUT PLAN")

        for exercise in generate_workout(goal, level):
            st.markdown(f"⚡ {exercise}")