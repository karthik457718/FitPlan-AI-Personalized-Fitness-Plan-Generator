import streamlit as st
import time

st.set_page_config(page_title="FitPlan AI Elite", page_icon="💎", layout="wide")

# ------------------------------
# THEME TOGGLE
# ------------------------------
theme = st.sidebar.toggle("🌙 Dark Mode", value=True)

if theme:
    overlay_color = "rgba(10,10,20,0.75)"
else:
    overlay_color = "rgba(255,255,255,0.65)"

# ------------------------------
# PREMIUM CSS
# ------------------------------
st.markdown(f"""
<style>

/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Outfit', sans-serif;
}}

/* Background with cinematic overlay */
[data-testid="stAppViewContainer"] {{
    background:
        linear-gradient({overlay_color}, {overlay_color}),
        url("https://images.unsplash.com/photo-1599058917765-a780eda07a3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Floating particles */
body::before {{
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,0,200,0.15) 2px, transparent 2px);
    background-size: 60px 60px;
    animation: moveParticles 60s linear infinite;
    z-index: 0;
}}

@keyframes moveParticles {{
    from {{ transform: translate(0,0); }}
    to {{ transform: translate(-300px,-300px); }}
}}

/* Center Layout */
.block-container {{
    max-width: 1150px;
    margin: auto;
    padding-top: 60px;
    position: relative;
    z-index: 1;
}}

/* Glass */
.glass {{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(30px);
    border-radius: 30px;
    padding: 40px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 0 60px rgba(255,0,200,0.25);
    margin-bottom: 35px;
}}

/* Neon animated border */
.glass:hover {{
    border: 1px solid transparent;
    background-clip: padding-box;
    position: relative;
}}

.glass:hover::before {{
    content: "";
    position: absolute;
    inset: -2px;
    border-radius: 30px;
    padding: 2px;
    background: linear-gradient(135deg, #ff00cc, #7928ca, #00f0ff);
    -webkit-mask:
        linear-gradient(#000 0 0) content-box,
        linear-gradient(#000 0 0);
    -webkit-mask-composite: xor;
            mask-composite: exclude;
}}

/* Inputs Glassy */
.stTextInput input,
.stNumberInput input,
.stSelectbox > div > div,
.stMultiSelect > div > div {{
    background: rgba(255,255,255,0.1) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    color: white !important;
}}

/* Button */
.stButton > button {{
    background: linear-gradient(135deg, #ff00cc, #7928ca);
    border-radius: 50px;
    padding: 14px 45px;
    border: none;
    font-weight: 600;
    color: white;
    box-shadow: 0 15px 40px rgba(255,0,200,0.5);
    transition: 0.3s ease;
}}

.stButton > button:hover {{
    transform: translateY(-5px);
    box-shadow: 0 20px 60px rgba(255,0,200,0.7);
}}

h1 {{
    text-align: center;
    font-size: 50px !important;
    font-weight: 700 !important;
    color: white !important;
}}

h2, h3, h4, p, label {{
    color: white !important;
}}

</style>
""", unsafe_allow_html=True)

# ------------------------------
# HERO
# ------------------------------
st.markdown("<h1>💎 FitPlan AI Elite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Train Smart. Perform Elite.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1,1], gap="large")

# ------------------------------
# FORM
# ------------------------------
with col1:
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

# ------------------------------
# LOGIC
# ------------------------------
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

# ------------------------------
# RESULTS
# ------------------------------
with col2:
    if generate:
        if name.strip() == "" or height_cm <= 0 or weight_kg <= 0:
            st.error("Please fill all fields properly.")
        else:
            bmi = calculate_bmi(height_cm, weight_kg)
            category = bmi_category(bmi)

            st.markdown('<div class="glass">', unsafe_allow_html=True)

            st.subheader(f"{name}")
            st.markdown(f"## BMI: {bmi}")
            st.markdown(f"### Category: {category}")

            # Animated BMI Progress
            progress = min(bmi / 40, 1.0)
            bar = st.progress(0)
            for i in range(int(progress * 100)):
                time.sleep(0.01)
                bar.progress(i + 1)

            st.markdown('</div>', unsafe_allow_html=True)