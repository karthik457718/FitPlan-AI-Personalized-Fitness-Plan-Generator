import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
    page_title="AI Fitness Planner",
    page_icon="💪",
    layout="wide"
)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_fitness = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_tutvdkg0.json"
)

st.markdown("""
<style>
body {
    background: linear-gradient(-45deg, #6a11cb, #2575fc, #00c6ff, #f7971e);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.main {
    background: rgba(255, 255, 255, 0.85);
    padding: 30px;
    border-radius: 25px;
    backdrop-filter: blur(10px);
}

.floating {
    position: fixed;
    font-size: 40px;
    animation: float 6s ease-in-out infinite;
    opacity: 0.12;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-25px); }
    100% { transform: translateY(0px); }
}

.icon1 { top: 10%; left: 5%; }
.icon2 { top: 60%; right: 8%; animation-delay: 2s; }
.icon3 { bottom: 10%; left: 40%; animation-delay: 4s; }

.card {
    padding: 20px;
    border-radius: 18px;
    background: white;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
    margin-bottom: 15px;
    font-weight: 500;
    font-size: 17px;
}

.stButton>button {
    background: linear-gradient(90deg, #6a11cb, #2575fc);
    color: white;
    border-radius: 12px;
    padding: 12px 30px;
    border: none;
    font-weight: 600;
    font-size: 16px;
}
</style>

<div class="floating icon1">🏋️</div>
<div class="floating icon2">💪</div>
<div class="floating icon3">🔥</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.title("💪 AI Fitness Planner")
    st.markdown("### Build your personalized workout plan")
    st.markdown("---")

with col2:
    if lottie_fitness:
        st_lottie(lottie_fitness, height=250)

st.subheader("🎯 Customize Your Plan")

col1, col2, col3 = st.columns(3)

with col1:
    goal = st.selectbox(
        "Select Your Goal",
        ["Flexible", "Weight Loss", "Build Muscle", "Strength Gaining", "Abs Building"]
    )

with col2:
    level = st.selectbox(
        "Fitness Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

with col3:
    duration = st.slider("Workout Duration (minutes)", 20, 120, 45)

equipment = st.multiselect(
    "🏋️ Select Available Equipment",
    [
        "Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment",
        "Inclined Bench", "Treadmill", "Cycle", "Skipping Rope",
        "Hand Gripper", "Pullups Bar", "Weight Plates",
        "Hula Hoop Ring", "Bosu Ball"
    ]
)

st.markdown("---")

def generate_workout(goal, level):

    plans = {
        "Weight Loss": [
            "Jump Rope – 3x2 min",
            "Treadmill Run – 15 min",
            "Burpees – 3x12",
            "Mountain Climbers – 3x20",
            "Cycling – 10 min"
        ],
        "Build Muscle": [
            "Dumbbell Squats – 4x12",
            "Incline Bench Press – 4x10",
            "Pullups – 3x8",
            "Dumbbell Shoulder Press – 3x12",
            "Resistance Band Rows – 3x15"
        ],
        "Strength Gaining": [
            "Deadlift – 5x5",
            "Pullups – 4x6",
            "Dumbbell Press – 4x6",
            "Hand Gripper – 3xMax",
            "Bosu Ball Squats – 3x10"
        ],
        "Abs Building": [
            "Plank – 3x60 sec",
            "Leg Raises – 3x15",
            "Russian Twists – 3x20",
            "Mountain Climbers – 3x25",
            "Bosu Ball Crunches – 3x15"
        ],
        "Flexible": [
            "Yoga Flow – 15 min",
            "Hamstring Stretch – 3x30 sec",
            "Hip Mobility – 10 min",
            "Cat-Cow – 3x15",
            "Balance Hold – 3x30 sec"
        ]
    }

    workout = plans.get(goal, [])

    if level == "Intermediate":
        workout = [exercise + " 🔥" for exercise in workout]
    elif level == "Advanced":
        workout = [exercise + " 💪🔥 (Increase weight/intensity)" for exercise in workout]

    return workout

if st.button("Generate Workout Plan 🚀"):

    st.subheader("🏆 Your Personalized Plan")
    plan = generate_workout(goal, level)

    for exercise in plan:
        st.markdown(f'<div class="card">✅ {exercise}</div>', unsafe_allow_html=True)

    st.success("Stay consistent. Results will follow! 💯🔥")