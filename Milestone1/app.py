import streamlit as st
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="FitPlan AI Elite", page_icon="💎", layout="wide")

# =============================
# GLOBAL STYLING
# =============================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Outfit', sans-serif;
}

/* Background */
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(rgba(10,10,20,0.55), rgba(10,10,20,0.55)),
        url("https://images.unsplash.com/photo-1599058917765-a780eda07a3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Center layout */
.block-container {
    max-width: 850px;
    margin: auto;
    padding-top: 60px;
}

/* Text */
h1, h2, h3, h4, p, label {
    color: white !important;
}

/* Glass Inputs */
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

/* Remove +/- background */
div[data-baseweb="input"] button {
    background: transparent !important;
    color: white !important;
}

/* Hover glow */
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

/* Neon Button */
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

</style>
""", unsafe_allow_html=True)

# =============================
# HERO
# =============================
st.markdown("<h1 style='text-align:center;'>💎 FitPlan AI Elite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Train Smart. Perform Elite.</p>", unsafe_allow_html=True)

# =============================
# FEATURE SECTION (FIXED VERSION)
# =============================
components.html("""
<div style="display:flex;align-items:center;justify-content:center;gap:40px;margin:70px 0;">

    <div style="width:220px;border-radius:25px;overflow:hidden;box-shadow:0 0 25px rgba(0,0,0,0.6);">
        <img src="https://images.unsplash.com/photo-1594737625785-a6cbdabd333c?auto=format&fit=crop&w=600&q=80"
             style="width:100%;border-radius:25px;">
    </div>

    <div style="
        max-width:600px;
        padding:35px;
        border-radius:25px;
        background:rgba(255,255,255,0.04);
        backdrop-filter:blur(25px);
        border:2px solid rgba(255,0,200,0.6);
        box-shadow:0 0 30px rgba(255,0,200,0.4);
        text-align:center;
        color:white;
    ">

        <h3 style="margin-bottom:25px;">🔥 Next-Gen AI Fitness Intelligence</h3>

        <div style="display:flex;justify-content:space-between;gap:25px;">

            <div>
                <div style="font-size:30px;">📊</div>
                <h4>Smart BMI</h4>
                <p>Precision tracking.</p>
            </div>

            <div>
                <div style="font-size:30px;">🏋️</div>
                <h4>AI Plans</h4>
                <p>Elite workouts.</p>
            </div>

            <div>
                <div style="font-size:30px;">⚡</div>
                <h4>Progression</h4>
                <p>Optimized growth.</p>
            </div>

        </div>
    </div>

    <div style="width:220px;border-radius:25px;overflow:hidden;box-shadow:0 0 25px rgba(0,0,0,0.6);">
        <img src="https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?auto=format&fit=crop&w=600&q=80"
             style="width:100%;border-radius:25px;">
    </div>

</div>
""", height=420)

# =============================
# FORM
# =============================
name = st.text_input("Full Name")
height_cm = st.number_input("Height (cm)", min_value=0, step=1)
weight_kg = st.number_input("Weight (kg)", min_value=0)

goal = st.selectbox("Goal",
    ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
)

level = st.selectbox("Level",
    ["Beginner", "Intermediate", "Advanced"]
)

equipment = st.multiselect("Equipment",
    ["Dumbbells", "Resistance Band", "Yoga Mat", "Bench", "Pullup Bar"]
)

generate = st.button("Generate Elite Plan 🚀")

# =============================
# LOGIC
# =============================
def calculate_bmi(height_cm, weight_kg):
    if height_cm == 0:
        return 0
    return round(weight_kg / ((height_cm/100) ** 2), 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def generate_workout(goal, level):
    base = {
        "Build Muscle": ["Squats – 4x12", "Bench Press – 4x10", "Pullups – 3x8"],
        "Weight Loss": ["Burpees – 3x15", "Jump Rope – 5 min", "Mountain Climbers – 3x20"],
        "Strength Gain": ["Deadlift – 5x5", "Overhead Press – 4x6"],
        "Abs Building": ["Plank – 3x60s", "Leg Raises – 3x15"],
        "Flexible": ["Yoga Flow – 20 min", "Stretching – 15 min"]
    }
    plan = base.get(goal, [])
    if level == "Intermediate":
        plan = [p + " 🔥" for p in plan]
    elif level == "Advanced":
        plan = [p + " 💪" for p in plan]
    return plan

# =============================
# RESULTS
# =============================
if generate:
    if name and height_cm > 0 and weight_kg > 0:
        bmi = calculate_bmi(height_cm, weight_kg)
        category = bmi_category(bmi)

        st.markdown("---")
        st.subheader(f"👤 {name}")
        st.markdown(f"### BMI: {bmi}")
        st.markdown(f"### Category: {category}")

        progress = min(bmi/40,1.0)
        bar = st.progress(0)
        for i in range(int(progress*100)):
            time.sleep(0.01)
            bar.progress(i+1)

        st.markdown("## 🏋️ Your Personalized Plan")
        for w in generate_workout(goal, level):
            st.markdown(f"✅ {w}")

        if equipment:
            st.markdown("### 🛠 Equipment Selected")
            st.write(", ".join(equipment))
    else:
        st.error("Please fill all required fields.")