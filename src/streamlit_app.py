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

/* ===== CENTER LAYOUT ===== */
.block-container {
    max-width: 850px;
    margin: auto;
    padding-top: 70px;
}

/* ===== TEXT COLORS ===== */
h1, h2, h3, h4, p, label {
    color: white !important;
}

/* ===== GLASS INPUTS (NO WHITE BOXES) ===== */
div[data-baseweb="input"] {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 30px !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    backdrop-filter: blur(15px);
}

div[data-baseweb="input"] > div {
    background: transparent !important;
}

div[data-baseweb="input"] input {
    background: transparent !important;
    color: white !important;
    border: none !important;
    box-shadow: none !important;
}

div[data-baseweb="input"] input:focus {
    background: transparent !important;
    outline: none !important;
}

/* Fix selectboxes */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 30px !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    backdrop-filter: blur(15px);
    color: white !important;
}

/* Remove number +/- white area */
div[data-baseweb="input"] button {
    background: transparent !important;
    color: white !important;
}

/* ===== ULTRA NEON BUTTON ===== */
.stButton > button {
    background: rgba(255,255,255,0.12) !important;
    border-radius: 40px !important;
    padding: 14px 45px !important;
    border: 2px solid rgba(255,255,255,0.4) !important;
    color: white !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

/* Neon Hover Effect */
.stButton > button:hover {
    background: linear-gradient(90deg, #ff00cc, #7928ca, #00f0ff) !important;
    background-size: 300% 300% !important;
    animation: neonMove 4s ease infinite !important;
    border: none !important;
    box-shadow:
        0 0 20px #ff00cc,
        0 0 40px #7928ca,
        0 0 60px #00f0ff !important;
    transform: translateY(-4px) scale(1.03) !important;
}

/* Glow Animation */
@keyframes neonMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

</style>
""", unsafe_allow_html=True)

# ===== HERO =====
st.markdown("<h1>💎 FitPlan AI Elite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Train Smart. Perform Elite.</p>", unsafe_allow_html=True)

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

generate = st.button("Generate Elite Plan 🚀")

# ===== BMI FUNCTIONS =====
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

# ===== WORKOUT GENERATOR =====
def generate_workout(goal, level):
    plans = {
        "Weight Loss": [
            "Jump Rope – 3x2 min",
            "Mountain Climbers – 3x20",
            "Burpees – 3x12",
            "Cycling – 10 min"
        ],
        "Build Muscle": [
            "Dumbbell Squats – 4x12",
            "Bench Press – 4x10",
            "Pullups – 3x8",
            "Shoulder Press – 3x12"
        ],
        "Strength Gain": [
            "Deadlifts – 5x5",
            "Pullups – 4x6",
            "Bench Press – 4x6"
        ],
        "Abs Building": [
            "Plank – 3x60 sec",
            "Leg Raises – 3x15",
            "Russian Twists – 3x20"
        ],
        "Flexible": [
            "Yoga Flow – 15 min",
            "Hamstring Stretch – 3x30 sec",
            "Hip Mobility – 10 min"
        ]
    }

    workout = plans.get(goal, [])

    if level == "Intermediate":
        workout = [w + " 🔥" for w in workout]
    elif level == "Advanced":
        workout = [w + " 💪 (Increase intensity)" for w in workout]

    return workout

# ===== RESULTS =====
if generate:
    if name.strip() == "" or height_cm <= 0 or weight_kg <= 0:
        st.error("Please complete all fields properly.")
    else:
        bmi = calculate_bmi(height_cm, weight_kg)
        category = bmi_category(bmi)

        st.subheader(f"👤 {name}")
        st.markdown(f"### BMI: {bmi}")
        st.markdown(f"### Category: {category}")

        progress = min(bmi / 40, 1.0)
        bar = st.progress(0)
        for i in range(int(progress * 100)):
            time.sleep(0.01)
            bar.progress(i + 1)

        st.markdown("---")
        st.subheader("🏋️ Your Personalized Workout Plan")

        workout_plan = generate_workout(goal, level)

        for exercise in workout_plan:
            st.markdown(f"✅ {exercise}")

        if equipment:
            st.markdown("### 🛠 Equipment Selected:")
            st.write(", ".join(equipment))