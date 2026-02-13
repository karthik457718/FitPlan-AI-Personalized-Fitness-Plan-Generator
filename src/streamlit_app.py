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

/* ===== CINEMATIC GYM BACKGROUND (Improved Visibility) ===== */
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(rgba(10,10,20,0.45), rgba(10,10,20,0.45)),
        url("https://images.unsplash.com/photo-1599058917765-a780eda07a3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* ===== CENTER LAYOUT ===== */
.block-container {
    max-width: 900px;
    margin: auto;
    padding-top: 70px;
}

/* ===== TEXT COLORS ===== */
h1, h2, h3, h4, p, label {
    color: white !important;
}

/* ============================= */
/* ===== GLASS INPUT STYLE ===== */
/* ============================= */

div[data-baseweb="input"],
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 30px !important;
    border: 2px solid rgba(255,255,255,0.35) !important;
    backdrop-filter: blur(15px);
    transition: all 0.3s ease !important;
}

/* Remove inner white */
div[data-baseweb="input"] > div {
    background: transparent !important;
}

/* Input text */
div[data-baseweb="input"] input {
    background: transparent !important;
    color: white !important;
    border: none !important;
    box-shadow: none !important;
}

/* Remove +/- white */
div[data-baseweb="input"] button {
    background: transparent !important;
    color: white !important;
}

/* ===== HOVER GLOW FOR INPUTS ===== */
div[data-baseweb="input"]:hover,
.stSelectbox > div > div:hover,
.stMultiSelect > div > div:hover {
    border: 2px solid transparent !important;
    background: linear-gradient(rgba(20,20,40,0.8), rgba(20,20,40,0.8)) padding-box,
                linear-gradient(90deg, #ff00cc, #7928ca, #00f0ff) border-box !important;
    box-shadow:
        0 0 15px #ff00cc,
        0 0 25px #7928ca,
        0 0 35px #00f0ff !important;
}

/* ============================= */
/* ===== NEON BUTTON ===== */
/* ============================= */

.stButton > button {
    background: rgba(255,255,255,0.12) !important;
    border-radius: 40px !important;
    padding: 14px 45px !important;
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
    transform: translateY(-4px) scale(1.03) !important;
}

@keyframes neonMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ============================= */
/* ===== FEATURE CARD ===== */
/* ============================= */

.feature-card {
    margin: 60px auto;
    padding: 50px;
    border-radius: 30px;
    position: relative;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(30px);
    border: 2px solid transparent;
}

.feature-card::before {
    content: "";
    position: absolute;
    inset: -3px;
    border-radius: 30px;
    padding: 3px;
    background: linear-gradient(90deg, #ff00cc, #7928ca, #00f0ff);
    background-size: 300% 300%;
    animation: borderMove 5s ease infinite;
    -webkit-mask:
        linear-gradient(#000 0 0) content-box,
        linear-gradient(#000 0 0);
    -webkit-mask-composite: xor;
            mask-composite: exclude;
}

@keyframes borderMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.feature-title {
    text-align: center;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 30px;
    color: white;
}

.feature-grid {
    display: flex;
    justify-content: space-between;
    gap: 30px;
}

.feature-item {
    flex: 1;
    text-align: center;
    color: white;
    transition: 0.3s ease;
}

.feature-item:hover {
    transform: translateY(-10px);
}

.feature-icon {
    font-size: 40px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

# ===== HERO =====
st.markdown("<h1 style='text-align:center;'>💎 FitPlan AI Elite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Train Smart. Perform Elite.</p>", unsafe_allow_html=True)

# ===== FEATURE CARD =====
st.markdown("""
<div class="feature-card">
    <div class="feature-title">🔥 Next-Gen AI Fitness Intelligence</div>
    <div class="feature-grid">
        <div class="feature-item">
            <div class="feature-icon">📊</div>
            <h4>Smart BMI Analysis</h4>
            <p>Precision health classification.</p>
        </div>
        <div class="feature-item">
            <div class="feature-icon">🏋️</div>
            <h4>Personalized Plans</h4>
            <p>AI-curated elite workouts.</p>
        </div>
        <div class="feature-item">
            <div class="feature-icon">⚡</div>
            <h4>Elite Progression</h4>
            <p>Optimized for transformation.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===== FORM =====
name = st.text_input("Full Name")

height_cm = st.number_input(
    "Height (cm)",
    min_value=1,
    value=170,
    step=1,
    format="%d"
)

weight_kg = st.number_input(
    "Weight (kg)",
    min_value=1,
    value=70,
    step=1,
    format="%d"
)

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
        "Weight Loss": ["Jump Rope – 3x2 min", "Burpees – 3x12"],
        "Build Muscle": ["Dumbbell Squats – 4x12", "Bench Press – 4x10"],
        "Strength Gain": ["Deadlifts – 5x5", "Pullups – 4x6"],
        "Abs Building": ["Plank – 3x60 sec", "Leg Raises – 3x15"],
        "Flexible": ["Yoga Flow – 15 min", "Hamstring Stretch – 3x30 sec"]
    }

    workout = plans.get(goal, [])

    if level == "Intermediate":
        workout = [w + " 🔥" for w in workout]
    elif level == "Advanced":
        workout = [w + " 💪 (Increase intensity)" for w in workout]

    return workout

# ===== RESULTS =====
if generate:
    if name.strip() == "":
        st.error("Please enter your name.")
    else:
        bmi = calculate_bmi(height_cm, weight_kg)
        category = bmi_category(bmi)

        st.markdown("---")
        st.subheader(f"👤 {name}")
        st.markdown(f"### BMI: {bmi}")
        st.markdown(f"### Category: {category}")

        progress = min(bmi / 40, 1.0)
        bar = st.progress(0)
        for i in range(int(progress * 100)):
            time.sleep(0.01)
            bar.progress(i + 1)

        st.markdown("## 🏋️ Your Workout Plan")
        workout_plan = generate_workout(goal, level)

        for exercise in workout_plan:
            st.markdown(f"✅ {exercise}")

        if equipment:
            st.markdown("### 🛠 Equipment Selected:")
            st.write(", ".join(equipment))