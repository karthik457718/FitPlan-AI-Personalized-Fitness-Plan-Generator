import streamlit as st
import time

st.set_page_config(page_title="FitPlan AI Ultra", page_icon="💎", layout="wide")

# ================== CSS ==================
st.markdown("""
<style>

/* ===== FONT ===== */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
}

/* ===== BACKGROUND ===== */
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(rgba(5,5,20,0.88), rgba(5,5,20,0.88)),
        url("https://images.unsplash.com/photo-1599058917765-a780eda07a3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* ===== CENTER ===== */
.block-container {
    max-width: 850px;
    margin: auto;
    padding-top: 70px;
}

/* ===== TEXT ===== */
h1, h2, h3, h4, p, label {
    color: white !important;
}

h1 {
    text-align: center;
    font-size: 42px !important;
    letter-spacing: 2px;
}

/* ===== REMOVE WHITE INPUTS ===== */
input, textarea {
    background-color: transparent !important;
    color: white !important;
}

div[data-baseweb="base-input"] {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 40px !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    backdrop-filter: blur(20px) !important;
}

div[data-baseweb="input"] {
    background: transparent !important;
}

input[type="text"],
input[type="number"] {
    background: transparent !important;
    color: white !important;
    box-shadow: none !important;
}

/* Autofill fix */
input:-webkit-autofill {
    -webkit-box-shadow: 0 0 0px 1000px transparent inset !important;
    -webkit-text-fill-color: white !important;
}

/* Remove white number area */
button[aria-label="Increase value"],
button[aria-label="Decrease value"] {
    background: transparent !important;
    color: white !important;
}

/* ===== SELECT GLASS ===== */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 40px !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    backdrop-filter: blur(20px) !important;
    color: white !important;
}

/* ===== NEON BUTTON ===== */
.stButton > button {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 50px !important;
    padding: 14px 50px !important;
    border: 2px solid rgba(255,255,255,0.4) !important;
    color: white !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #ff00cc, #7928ca, #00f0ff) !important;
    background-size: 300% 300% !important;
    animation: neonMove 4s ease infinite !important;
    border: none !important;
    box-shadow:
        0 0 20px #ff00cc,
        0 0 40px #7928ca,
        0 0 60px #00f0ff !important;
    transform: translateY(-4px) !important;
}

@keyframes neonMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

</style>
""", unsafe_allow_html=True)

# ================== HERO ==================
st.markdown("<h1>💎 FITPLAN AI ULTRA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>FUTURISTIC FITNESS INTELLIGENCE</p>", unsafe_allow_html=True)

# ================== FORM ==================
name = st.text_input("Full Name")
height_cm = st.number_input("Height (cm)", min_value=0.0)
weight_kg = st.number_input("Weight (kg)", min_value=0.0)

goal = st.selectbox(
    "Goal",
    ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
)

level = st.selectbox(
    "Level",
    ["Beginner", "Intermediate", "Advanced"]
)

equipment = st.multiselect(
    "Equipment",
    ["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment",
     "Bench", "Treadmill", "Cycle", "Pullup Bar"]
)

generate = st.button("Generate Ultra Plan 🚀")

# ================== BMI ==================
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

# ================== WORKOUT ==================
def generate_workout(goal, level):
    plans = {
        "Weight Loss": ["HIIT Sprint – 15 min", "Burpees – 3x15", "Mountain Climbers – 3x20"],
        "Build Muscle": ["Bench Press – 4x10", "Squats – 4x12", "Pullups – 3x8"],
        "Strength Gain": ["Deadlifts – 5x5", "Heavy Pullups – 4x6"],
        "Abs Building": ["Planks – 3x60 sec", "Leg Raises – 3x15"],
        "Flexible": ["Yoga Flow – 20 min", "Mobility Training – 15 min"]
    }

    workout = plans.get(goal, [])

    if level == "Intermediate":
        workout = [w + " 🔥" for w in workout]
    elif level == "Advanced":
        workout = [w + " 💎 ELITE" for w in workout]

    return workout

# ================== RESULTS ==================
if generate:
    if name.strip() == "" or height_cm <= 0 or weight_kg <= 0:
        st.error("Please complete all fields properly.")
    else:
        bmi = calculate_bmi(height_cm, weight_kg)
        category = bmi_category(bmi)

        st.markdown("---")
        st.subheader(f"👤 {name}")
        st.markdown(f"### BMI: {bmi}")
        st.markdown(f"### Category: {category}")

        st.markdown("---")
        st.subheader("🏋️ ULTRA WORKOUT PLAN")

        for exercise in generate_workout(goal, level):
            st.markdown(f"⚡ {exercise}")