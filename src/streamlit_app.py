import streamlit as st

st.set_page_config(
    page_title="AI Fitness Planner",
    page_icon="💪",
    layout="wide"
)

st.markdown("""
<style>

/* Full Animated Gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, 
        #667eea 0%, 
        #764ba2 25%, 
        #6B73FF 50%, 
        #000DFF 75%, 
        #667eea 100%);
    background-size: 300% 300%;
    animation: gradientMove 12s ease infinite;
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Glass Container */
.block-container {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 2rem;
}

/* Remove header background */
[data-testid="stHeader"] {
    background: transparent;
}

/* White Text */
h1, h2, h3, label, p {
    color: white !important;
}

/* Inputs */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.2) !important;
    color: white !important;
    border-radius: 10px;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    border-radius: 12px;
    padding: 12px 28px;
    border: none;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


col1, col2 = st.columns([2, 1])

with col1:
    st.title("💪 AI Fitness Planner")
    st.markdown("### Build your personalized workout plan")
    st.markdown("---")

with col2:
    st.components.v1.html("""
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player 
        src="https://assets9.lottiefiles.com/packages/lf20_tutvdkg0.json"
        background="transparent"
        speed="1"
        style="width: 280px; height: 280px;"
        loop
        autoplay>
    </lottie-player>
    """, height=280)


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
        st.markdown(f"""
        <div style="
            padding:15px;
            margin-bottom:10px;
            background:rgba(255,255,255,0.15);
            border-radius:12px;
            color:white;">
            ✅ {exercise}
        </div>
        """, unsafe_allow_html=True)

    st.success("Stay consistent. Results will follow! 💯🔥")