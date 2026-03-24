import streamlit as st
import os, sys, json, base64
from datetime import date, timedelta
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from auth_token import logout

st.set_page_config(page_title="Workout Plan | FitPlan Pro", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

if not st.session_state.get("logged_in"):
    st.switch_page("app.py")
if "user_data" not in st.session_state:
    st.switch_page("pages/1_Profile.py")

uname   = st.session_state.get("username", "Athlete")
data    = st.session_state.user_data
plan_id = st.session_state.get("plan_id", "")

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow+Condensed:wght@700;800;900&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap');
#MainMenu,footer,header,[data-testid="stToolbar"],[data-testid="stDecoration"],
[data-testid="stSidebarNav"],section[data-testid="stSidebar"]{display:none!important;}
html,body,.stApp{background:#0d0806!important;color:#fff!important;font-family:'DM Sans',sans-serif!important;}
[data-testid="stAppViewContainer"]{
  background:linear-gradient(180deg,rgba(8,5,3,0.50) 0%,rgba(8,5,3,0.42) 40%,rgba(8,5,3,0.55) 100%),
    url('https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1800&q=80&auto=format&fit=crop')
    center center/cover no-repeat fixed!important;}
[data-testid="stAppViewContainer"]>section>div.block-container{
  max-width:1100px!important;margin:0 auto!important;padding:0 24px 100px!important;}
[data-testid="stWidgetLabel"],[data-testid="stWidgetLabel"] p,.stCheckbox>label{
  color:#fff!important;font-size:0.78rem!important;font-weight:700!important;
  letter-spacing:2px!important;text-transform:uppercase!important;text-shadow:0 1px 10px rgba(0,0,0,0.95)!important;}
.stTextArea>div>div>textarea{background:rgba(10,5,3,0.70)!important;
  border:1px solid rgba(229,9,20,0.25)!important;color:#fff!important;border-radius:10px!important;}
/* Nav buttons */
div[data-testid="stHorizontalBlock"]:first-of-type div[data-testid="stButton"] > button{
  background:rgba(18,4,4,0.82)!important;border:1.5px solid rgba(229,9,20,0.50)!important;
  color:rgba(255,255,255,0.92)!important;border-radius:9px!important;
  font-family:'DM Sans',sans-serif!important;font-size:0.68rem!important;font-weight:700!important;
  padding:5px 8px!important;height:32px!important;min-height:32px!important;
  white-space:nowrap!important;box-shadow:0 0 8px rgba(229,9,20,0.22)!important;
  transition:all 0.15s ease!important;text-transform:none!important;}
div[data-testid="stHorizontalBlock"]:first-of-type div[data-testid="stButton"] > button:hover{
  background:rgba(229,9,20,0.28)!important;border-color:rgba(229,9,20,0.85)!important;
  color:#fff!important;box-shadow:0 0 18px rgba(229,9,20,0.60)!important;transform:translateY(-1px)!important;}
div[data-testid="stHorizontalBlock"]:first-of-type div[data-testid="stButton"]:last-child > button{
  background:linear-gradient(135deg,#c0000c,#8b0000)!important;
  border-color:rgba(229,9,20,0.80)!important;animation:so-p 2.6s ease-in-out infinite!important;}
div[data-testid="stHorizontalBlock"]:first-of-type div[data-testid="stButton"]:last-child > button:hover{
  background:linear-gradient(135deg,#E50914,#b0000a)!important;
  box-shadow:0 0 28px rgba(229,9,20,0.95)!important;animation:none!important;}
@keyframes so-p{0%,100%{box-shadow:0 0 12px rgba(229,9,20,0.55);}50%{box-shadow:0 0 24px rgba(229,9,20,0.88);}}
/* Content buttons */
.stButton>button{background:linear-gradient(135deg,rgba(229,9,20,0.85),rgba(160,0,10,0.90))!important;
  border:1.5px solid rgba(229,9,20,0.60)!important;color:#fff!important;border-radius:10px!important;
  font-family:'DM Sans',sans-serif!important;font-size:0.85rem!important;font-weight:700!important;
  box-shadow:0 0 16px rgba(229,9,20,0.40)!important;transition:all 0.25s!important;}
.stButton>button:hover{transform:translateY(-2px) scale(1.02)!important;
  box-shadow:0 0 28px rgba(229,9,20,0.65)!important;}
.stTabs [data-baseweb="tab-list"]{background:rgba(255,255,255,0.04)!important;
  border-radius:10px!important;padding:4px!important;gap:3px!important;
  border:1px solid rgba(255,255,255,0.07)!important;}
.stTabs [data-baseweb="tab"]{background:transparent!important;color:rgba(255,255,255,0.42)!important;
  border-radius:7px!important;font-family:'DM Sans',sans-serif!important;font-size:0.78rem!important;
  font-weight:600!important;border:none!important;padding:9px 16px!important;}
.stTabs [aria-selected="true"]{background:linear-gradient(135deg,#E50914,#c0000c)!important;
  color:#fff!important;box-shadow:0 3px 12px rgba(229,9,20,0.40)!important;}
.stTabs [data-baseweb="tab-highlight"],.stTabs [data-baseweb="tab-border"]{display:none!important;}
.nav-wrap{background:rgba(5,2,1,0.97);backdrop-filter:blur(20px);
  border-bottom:1.5px solid rgba(229,9,20,0.22);box-shadow:0 2px 24px rgba(0,0,0,0.65);
  padding:5px 0;margin-bottom:4px;}
.nav-logo{font-family:'Bebas Neue',sans-serif;font-size:1.4rem;letter-spacing:5px;
  color:#E50914;text-shadow:0 0 18px rgba(229,9,20,0.45);line-height:1;}
.hero{background:linear-gradient(135deg,rgba(229,9,20,0.20),rgba(120,0,8,0.12) 40%,rgba(10,5,3,0.55));
  border:1px solid rgba(229,9,20,0.32);border-radius:18px;padding:36px 44px;margin:20px 0 28px;
  position:relative;overflow:hidden;backdrop-filter:blur(2px);}
.hero::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,#E50914,transparent);}
.hero-title{font-family:'Barlow Condensed',sans-serif;font-size:clamp(2rem,5vw,3.8rem);
  font-weight:900;text-transform:uppercase;color:#fff;line-height:1;margin-bottom:10px;}
.hero-title span{color:#E50914;}
.stat-row{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-bottom:32px;}
.stat{background:rgba(10,6,4,0.55);border:1px solid rgba(229,9,20,0.18);border-radius:12px;
  padding:18px 12px;text-align:center;backdrop-filter:blur(18px);position:relative;overflow:hidden;}
.stat::before{content:'';position:absolute;top:0;left:0;right:0;height:1.5px;
  background:linear-gradient(90deg,transparent,rgba(229,9,20,0.45),transparent);}
.stat-lbl{font-size:0.55rem;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;
  color:rgba(255,255,255,0.38);margin-bottom:8px;}
.stat-val{font-family:'Bebas Neue',sans-serif;font-size:2rem;color:#fff;letter-spacing:1px;}
.stat-unit{font-size:0.60rem;color:rgba(255,255,255,0.35);margin-top:4px;}
.day-card{background:rgba(10,6,4,0.62);border:1px solid rgba(229,9,20,0.15);
  border-radius:16px;padding:28px 32px;backdrop-filter:blur(16px);position:relative;overflow:hidden;}
.day-card::before{content:'';position:absolute;top:0;left:0;right:0;height:1.5px;
  background:linear-gradient(90deg,transparent,rgba(229,9,20,0.40),transparent);}
.sec-title{font-size:0.60rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;
  color:rgba(229,9,20,0.75);margin:20px 0 14px;display:flex;align-items:center;gap:8px;}
.sec-title::before{content:'';width:16px;height:1.5px;background:#E50914;border-radius:1px;}
.sec-title::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,rgba(229,9,20,0.18),transparent);}
.badge{display:inline-flex;flex-direction:column;align-items:center;
  min-width:48px;padding:5px 10px;border-radius:7px;line-height:1.2;}
.badge-num{font-size:0.88rem;font-weight:800;}
.badge-lbl{font-size:0.46rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;opacity:0.70;}
.b-sets{background:rgba(100,160,255,0.13);border:1px solid rgba(100,160,255,0.24);color:#93c5fd;}
.b-reps{background:rgba(100,230,180,0.11);border:1px solid rgba(100,230,180,0.21);color:#6ee7b7;}
.b-rest{background:rgba(255,180,80,0.11);border:1px solid rgba(255,180,80,0.21);color:#fdba74;}
.rest-day{text-align:center;padding:40px;background:rgba(229,9,20,0.06);
  border:1px solid rgba(229,9,20,0.18);border-radius:16px;}
.caution-box{background:rgba(251,191,36,0.08);border:1px solid rgba(251,191,36,0.28);
  border-radius:12px;padding:16px 20px;margin:14px 0;}
.meal-card{background:rgba(10,20,12,0.55);border:1px solid rgba(34,197,94,0.18);
  border-radius:12px;padding:14px 18px;margin-bottom:8px;}
.meal-lbl{font-size:0.58rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;
  color:rgba(34,197,94,0.70);margin-bottom:4px;}
.meal-txt{font-size:0.85rem;color:rgba(255,255,255,0.80);line-height:1.5;}
.stCheckbox{margin-top:4px!important;}
</style>
""", unsafe_allow_html=True)

# ── NAV ────────────────────────────────────────────────────────────────────────
st.markdown("<div class='nav-wrap'>", unsafe_allow_html=True)
_n = st.columns([1.8,1,1,1,1,1,1,1.3])
with _n[0]: st.markdown("<div class='nav-logo'>⚡ FITPLAN PRO</div>", unsafe_allow_html=True)
with _n[1]:
    if st.button("🏠 Home", key="nb_db", use_container_width=True):
        st.switch_page("pages/2_Dashboard.py")
with _n[2]:
    if st.button("● ⚡ Workout", key="nb_wp", use_container_width=True):
        st.switch_page("pages/3_Workout_Plan.py")
with _n[3]:
    if st.button("🥗 Diet", key="nb_dp", use_container_width=True):
        st.switch_page("pages/4_Diet_Plan.py")
with _n[4]:
    if st.button("🤖 AI Coach", key="nb_ai", use_container_width=True):
        try: st.switch_page("pages/5_ai_coach.py")
        except Exception as e: st.warning(f"Upload 5_AI_Coach.py: {e}")
with _n[5]:
    if st.button("🏆 Records", key="nb_rc", use_container_width=True):
        try: st.switch_page("pages/6_records.py")
        except Exception as e: st.warning(f"Upload 6_Records.py: {e}")
with _n[6]:
    if st.button("📸 Photos", key="nb_ph", use_container_width=True):
        try: st.switch_page("pages/7_progress_photos.py")
        except Exception as e: st.warning(f"Upload 7_Progress_Photos.py: {e}")
with _n[7]:
    if st.button("🚪 Sign Out", key="nb_so", use_container_width=True):
        logout(uname)
        for _k in ["logged_in","username","auth_token","user_data","workout_plan",
                   "structured_days","dietary_type","full_plan_data","plan_id","plan_start",
                   "plan_duration","plan_for","force_regen","tracking","_plan_checked",
                   "_db_loaded_dash","_auto_redirect","_diet_chosen","_needs_rerun",
                   "_db_streak","edit_profile_mode","_login_db_err","_notes_loaded"]:
            st.session_state.pop(_k, None)
        st.switch_page("app.py")
st.markdown("</div>", unsafe_allow_html=True)

# ── VARIABLES ─────────────────────────────────────────────────────────────────
sdays        = st.session_state.get("structured_days", [])
dietary_type = st.session_state.get("dietary_type", "veg")

from prompt_builder import calculate_bmi, bmi_category
bmi     = calculate_bmi(data["weight"], data["height"])
bmi_cat = bmi_category(bmi)

# ── PLAN GENERATION ───────────────────────────────────────────────────────────
need_gen = (not sdays) or st.session_state.get("force_regen", False)

if need_gen:
    # Step 1 — choose diet type if not already chosen
    if "dietary_type" not in st.session_state or st.session_state.get("force_regen"):
        st.markdown("""
        <div style='max-width:520px;margin:50px auto 0;text-align:center'>
          <div style='font-family:Bebas Neue,sans-serif;font-size:2.4rem;letter-spacing:3px;color:#fff;margin-bottom:8px'>Choose Your Diet Type</div>
          <div style='font-size:0.85rem;color:rgba(255,255,255,0.45);margin-bottom:32px'>Your meals will be tailored to your preference</div>
        </div>
        """, unsafe_allow_html=True)
        dc1, dc2, dc3 = st.columns(3)
        with dc1:
            st.markdown("<div style='background:rgba(5,40,15,0.80);border:2px solid rgba(34,197,94,0.45);border-radius:14px;padding:20px;text-align:center;margin-bottom:10px'><div style='font-size:2.5rem'>&#127807;</div><div style='font-family:Bebas Neue,sans-serif;font-size:1.2rem;color:#22c55e;letter-spacing:2px;margin-top:8px'>Vegetarian</div><div style='font-size:0.72rem;color:rgba(255,255,255,0.45);margin-top:4px'>Plant-based meals</div></div>", unsafe_allow_html=True)
            if st.button("Select Veg", use_container_width=True, key="pick_veg"):
                st.session_state.dietary_type = "veg"
                st.session_state.pop("force_regen", None)
                st.rerun()
        with dc2:
            st.markdown("<div style='background:rgba(50,15,5,0.80);border:2px solid rgba(249,115,22,0.45);border-radius:14px;padding:20px;text-align:center;margin-bottom:10px'><div style='font-size:2.5rem'>&#127829;</div><div style='font-family:Bebas Neue,sans-serif;font-size:1.2rem;color:#f97316;letter-spacing:2px;margin-top:8px'>Non-Vegetarian</div><div style='font-size:0.72rem;color:rgba(255,255,255,0.45);margin-top:4px'>High-protein meals</div></div>", unsafe_allow_html=True)
            if st.button("Select Non-Veg", use_container_width=True, key="pick_nveg"):
                st.session_state.dietary_type = "nonveg"
                st.session_state.pop("force_regen", None)
                st.rerun()
        with dc3:
            st.markdown("<div style='background:rgba(20,35,5,0.80);border:2px solid rgba(250,204,21,0.40);border-radius:14px;padding:20px;text-align:center;margin-bottom:10px'><div style='font-size:2.5rem'>&#127807;&#127829;</div><div style='font-family:Bebas Neue,sans-serif;font-size:1.2rem;color:#facc15;letter-spacing:2px;margin-top:8px'>Both / Flexible</div><div style='font-size:0.72rem;color:rgba(255,255,255,0.45);margin-top:4px'>Mixed meals</div></div>", unsafe_allow_html=True)
            if st.button("Select Flexible", use_container_width=True, key="pick_both"):
                st.session_state.dietary_type = "both"
                st.session_state.pop("force_regen", None)
                st.rerun()
        st.stop()

    # Step 2 — Generate the plan
    dietary_type  = st.session_state.get("dietary_type", "veg")
    total_days_gen = data.get("total_days", 28)
    days_per_week  = data.get("days_per_week", 5)
    months_val     = data.get("months", 1)
    # Recalculate to ensure correct value
    if days_per_week and months_val:
        total_days_gen = days_per_week * 4 * months_val

    diet_label = {"veg":"🌿 Vegetarian","nonveg":"🍗 Non-Vegetarian","both":"🌿🍗 Flexible"}.get(dietary_type,"Vegetarian")

    st.markdown(
        "<div style='max-width:600px;margin:50px auto 0;text-align:center'>"
        "<div style='font-family:Bebas Neue,sans-serif;font-size:2.4rem;letter-spacing:3px;color:#fff;margin-bottom:8px'>Generating Your Plan</div>"
        "<div style='display:inline-block;padding:4px 16px;border-radius:20px;background:rgba(229,9,20,0.12);border:1px solid rgba(229,9,20,0.30);color:#E50914;margin-bottom:12px;font-size:0.80rem;font-weight:700'>"
        + diet_label + "</div>"
        "<div style='font-size:0.82rem;color:rgba(255,255,255,0.42);margin-bottom:24px'>"
        "Building your <b style='color:#E50914'>" + str(total_days_gen) + "-day</b> "
        "(" + str(days_per_week) + " days/week &times; " + str(months_val) + " month) workout + diet plan &#9889;</div>"
        "</div>",
        unsafe_allow_html=True
    )

    prog = st.progress(0, text="Starting...")
    sph  = st.empty()

    def _gen_cb(cn, tc, dd, td, status=None):
        pct = min(int((cn-1)/max(tc,1)*100), 99)
        prog.progress(pct, text=status or ("Generating Day " + str(dd+1) + " of " + str(td) + "..."))
        sph.markdown("<div style='text-align:center;font-size:0.68rem;color:rgba(255,255,255,0.28)'>Chunk " + str(cn) + "/" + str(tc) + "</div>", unsafe_allow_html=True)

    try:
        from model_api import query_model_chunked
        wplan, new_sdays, _b, _bc = query_model_chunked(
            name=data["name"], gender=data["gender"],
            height=data["height"], weight=data["weight"],
            goal=data["goal"], fitness_level=data["level"],
            equipment=data.get("equipment", []),
            days_per_week=days_per_week, months=months_val,
            dietary_type=dietary_type,
            progress_callback=_gen_cb
        )
        prog.progress(100, text="✅ Plan Ready!")
        sph.empty()

        # Renumber days sequentially
        for _i, _d in enumerate(new_sdays):
            _d["day"] = _i + 1

        # Save everything to session state FIRST
        st.session_state.structured_days = new_sdays
        st.session_state.full_plan_data  = new_sdays
        st.session_state.workout_plan    = wplan
        st.session_state.plan_for        = uname
        st.session_state.dietary_type    = dietary_type
        st.session_state.pop("force_regen", None)
        st.session_state.pop("_plan_checked", None)
        st.session_state.pop("_db_loaded_dash", None)

        if "plan_start" not in st.session_state:
            st.session_state.plan_start = date.today().isoformat()

        # Save to DB in a completely isolated try — never affects the rerun
        _saved_pid = None
        try:
            from utils.db import save_plan as _sp
            _saved_pid = _sp(uname, dietary_type, total_days_gen, new_sdays)
        except Exception:
            pass
        if _saved_pid:
            st.session_state.plan_id = _saved_pid

        # Show success banner then rerun immediately
        prog.empty()
        sph.empty()
        st.markdown(
            "<div style='max-width:500px;margin:16px auto;text-align:center;"
            "background:rgba(34,197,94,0.12);border:1.5px solid rgba(34,197,94,0.40);"
            "border-radius:14px;padding:18px 24px;backdrop-filter:blur(10px)'>"
            "<div style='font-size:1.8rem;margin-bottom:8px'>🎉</div>"
            "<div style='font-family:Bebas Neue,sans-serif;font-size:1.6rem;color:#22c55e;"
            "letter-spacing:2px'>Plan Ready!</div>"
            "<div style='font-size:0.82rem;color:rgba(255,255,255,0.55);margin-top:6px'>"
            "Your " + str(len(new_sdays)) + "-day plan has been generated. Loading now...</div>"
            "</div>",
            unsafe_allow_html=True
        )
        import time as _time
        _time.sleep(1.5)
        st.rerun()

    except Exception as _gen_err:
        # Only reach here if query_model_chunked itself failed
        try: prog.empty()
        except Exception: pass
        try: sph.empty()
        except Exception: pass
        _err_msg = str(_gen_err)
        st.markdown(
            "<div style='max-width:560px;margin:20px auto;background:rgba(229,9,20,0.10);"
            "border:1px solid rgba(229,9,20,0.30);border-radius:14px;padding:24px 28px'>"
            "<div style='font-size:1rem;font-weight:700;color:#ff6b6b;margin-bottom:8px'>"
            "&#9888; Generation Failed</div>"
            "<div style='font-size:0.82rem;color:rgba(255,255,255,0.60);line-height:1.7'>"
            + _err_msg + "</div>"
            "<div style='margin-top:12px;font-size:0.72rem;color:rgba(255,255,255,0.35)'>"
            "Tip: Check your GROQ_API_KEY in HuggingFace Secrets, or reduce days/week in Profile.</div>"
            "</div>",
            unsafe_allow_html=True
        )
        _c1, _c2 = st.columns(2)
        with _c1:
            if st.button("&#8592; Back to Profile", key="gen_fail_prof"):
                st.switch_page("pages/1_Profile.py")
        with _c2:
            if st.button("&#8635; Try Again", key="gen_fail_retry"):
                st.session_state.pop("structured_days", None)
                st.rerun()
        st.stop()

# ── HERO ──────────────────────────────────────────────────────────────────────
total_days = len(sdays)
st.markdown(f"""
<div class='hero'>
  <div style='font-size:0.60rem;font-weight:700;letter-spacing:4px;text-transform:uppercase;
    color:rgba(229,9,20,0.75);margin-bottom:10px'>⚡ Personalised AI Fitness Plan</div>
  <div class='hero-title'>{data['name'].upper()}'S <span>{total_days}-DAY PLAN</span></div>
  <div style='font-size:0.85rem;color:rgba(255,255,255,0.45);display:flex;gap:12px;flex-wrap:wrap'>
    <span>🎯 {data['goal']}</span>
    <span>·</span><span>📊 {data['level']}</span>
    <span>·</span><span>⚖️ BMI {bmi:.1f} · {bmi_cat}</span>
    <span>·</span><span>{'🌿 Vegetarian' if dietary_type=='veg' else '🍗 Non-Veg'}</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── STAT CARDS ────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class='stat-row'>
  <div class='stat'><div class='stat-lbl'>🎂 Age</div><div class='stat-val'>{data['age']}</div><div class='stat-unit'>years</div></div>
  <div class='stat'><div class='stat-lbl'>📏 Height</div><div class='stat-val'>{data['height']}</div><div class='stat-unit'>cm</div></div>
  <div class='stat'><div class='stat-lbl'>⚖️ Weight</div><div class='stat-val'>{data['weight']}</div><div class='stat-unit'>kg</div></div>
  <div class='stat'><div class='stat-lbl'>📈 BMI</div><div class='stat-val'>{bmi:.1f}</div><div class='stat-unit'>{bmi_cat}</div></div>
  <div class='stat'><div class='stat-lbl'>🎯 Goal</div><div class='stat-val' style='font-size:1.1rem;line-height:1.2'>{data['goal']}</div><div class='stat-unit'>{data['level']}</div></div>
</div>
""", unsafe_allow_html=True)

# ── SAFETY + PDF ──────────────────────────────────────────────────────────────
with st.expander("⚠️ Safety Cautions — Read Before Starting", expanded=False):
    st.markdown("""
    <div class='caution-box'>
      <div style='font-size:0.60rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:rgba(251,191,36,0.80);margin-bottom:12px'>⚠ WORKOUT SAFETY REMINDERS</div>
      <div style='display:grid;grid-template-columns:1fr 1fr;gap:8px'>
        <div style='font-size:0.82rem;color:rgba(255,255,255,0.72);padding:6px 0;border-bottom:1px solid rgba(255,255,255,0.05)'>🧘 Maintain correct posture throughout</div>
        <div style='font-size:0.82rem;color:rgba(255,255,255,0.72);padding:6px 0;border-bottom:1px solid rgba(255,255,255,0.05)'>💧 Stay hydrated — drink water regularly</div>
        <div style='font-size:0.82rem;color:rgba(255,255,255,0.72);padding:6px 0;border-bottom:1px solid rgba(255,255,255,0.05)'>🔥 Always warm up before starting</div>
        <div style='font-size:0.82rem;color:rgba(255,255,255,0.72);padding:6px 0;border-bottom:1px solid rgba(255,255,255,0.05)'>🛑 Stop immediately if pain occurs</div>
        <div style='font-size:0.82rem;color:rgba(255,255,255,0.72);padding:6px 0;border-bottom:1px solid rgba(255,255,255,0.05)'>😮‍💨 Breathe steadily — never hold breath</div>
        <div style='font-size:0.82rem;color:rgba(255,255,255,0.72);padding:6px 0'>⚖️ Use appropriate resistance level</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("📄 Export Plan as PDF", expanded=False):
    pdf_lines = [f"<h1>{data.get('name','').upper()}'S {total_days}-DAY FITNESS PLAN</h1>",
                 f"<p><b>Goal:</b> {data.get('goal','')} | <b>Level:</b> {data.get('level','')} | <b>Diet:</b> {'Veg' if dietary_type=='veg' else 'Non-Veg'}</p><hr>"]
    for d in sdays:
        dn = d.get('day',1); mg = d.get('muscle_group','Full Body')
        if d.get('is_rest_day'):
            pdf_lines.append(f"<h2>Day {dn} — Rest Day</h2><hr>")
        else:
            pdf_lines.append(f"<h2>Day {dn} — {mg}</h2><ul>")
            for ex in d.get('workout',[]):
                pdf_lines.append(f"<li><b>{ex.get('name','')}</b> — {ex.get('sets',3)}×{ex.get('reps','12')} (rest {ex.get('rest','60s')})</li>")
            pdf_lines.append("</ul><hr>")
    full_html = ("<html><head><style>body{font-family:Arial;font-size:13px;max-width:800px;margin:0 auto;padding:20px}"
                 "h1{color:#c0000c}h2{border-bottom:1px solid #ddd;padding-bottom:4px}</style></head><body>"
                 + "".join(pdf_lines) + "</body></html>")
    b64 = base64.b64encode(full_html.encode()).decode()
    st.markdown(f"<a href='data:text/html;base64,{b64}' download='fitplan_{data.get('name','plan').lower()}.html' "
                f"style='display:inline-block;background:#E50914;color:#fff;padding:10px 24px;"
                f"border-radius:10px;font-weight:700;text-decoration:none'>📄 Download Plan (Open → Ctrl+P → Save PDF)</a>",
                unsafe_allow_html=True)

# ── PROGRESS HEATMAP ─────────────────────────────────────────────────────────
st.markdown("<div class='sec-title'>Your Workout Schedule</div>", unsafe_allow_html=True)

completed_days = []
for _d in sdays:
    _dn   = _d.get("day", 0)
    _ex   = _d.get("workout", [])
    _rest = _d.get("is_rest_day", False)
    if _rest:
        completed_days.append("rest")
    elif all(st.session_state.get(f"ex_d{_dn}_{_i}", False) for _i in range(len(_ex))) and len(_ex) > 0:
        completed_days.append("done")
    else:
        try:
            from utils.db import get_progress
            prog = get_progress(uname, plan_id, _dn)
            if prog.get("day_completed"):
                completed_days.append("done")
                for _i in range(len(_ex)): st.session_state[f"ex_d{_dn}_{_i}"] = True
            else: completed_days.append("pending")
        except Exception: completed_days.append("pending")

done_count = completed_days.count("done")
pct_done   = int(done_count / max(total_days,1) * 100)

heatmap_cells = ""
for _i, _status in enumerate(completed_days):
    _dn2 = sdays[_i].get("day",_i+1)
    if _status=="done":    col="#22c55e";  bg="rgba(34,197,94,0.25)";  brd="rgba(34,197,94,0.55)"
    elif _status=="rest":  col="#94a3b8";  bg="rgba(148,163,184,0.15)";brd="rgba(148,163,184,0.30)"
    else:                  col="rgba(255,255,255,0.25)";bg="rgba(255,255,255,0.05)";brd="rgba(255,255,255,0.10)"
    heatmap_cells += (f"<div title='Day {_dn2}' style='width:28px;height:28px;border-radius:5px;"
                      f"background:{bg};border:1.5px solid {brd};display:flex;align-items:center;"
                      f"justify-content:center;font-size:0.55rem;font-weight:700;color:{col}'>{_dn2}</div>")

st.markdown(f"""
<div style='background:rgba(10,6,4,0.60);border:1px solid rgba(229,9,20,0.15);
  border-radius:16px;padding:20px 24px;margin-bottom:24px;position:relative;overflow:hidden'>
  <div style='position:absolute;top:0;left:0;right:0;height:1.5px;
    background:linear-gradient(90deg,transparent,rgba(229,9,20,0.40),transparent)'></div>
  <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:14px'>
    <span style='font-size:0.60rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:rgba(229,9,20,0.75)'>
      📊 Progress — {done_count}/{total_days} days completed</span>
    <span style='font-family:Bebas Neue,sans-serif;font-size:1.6rem;color:#E50914'>{pct_done}%</span>
  </div>
  <div style='height:8px;background:rgba(255,255,255,0.07);border-radius:4px;overflow:hidden;margin-bottom:14px'>
    <div style='height:100%;width:{pct_done}%;background:linear-gradient(90deg,#E50914,#ff4444);border-radius:4px'></div>
  </div>
  <div style='display:flex;flex-wrap:wrap;gap:4px'>{heatmap_cells}</div>
  <div style='display:flex;gap:16px;margin-top:10px;font-size:0.65rem;color:rgba(255,255,255,0.35)'>
    <span><span style='color:#22c55e'>■</span> Completed</span>
    <span><span style='color:#94a3b8'>■</span> Rest Day</span>
    <span><span style='color:rgba(255,255,255,0.25)'>■</span> Pending</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SOCIAL SHARE CARD ─────────────────────────────────────────────────────────
with st.expander("🎉 Share Your Progress", expanded=False):
    streak_val = st.session_state.get("_db_streak", 0)
    st.markdown(f"""
<div style='background:linear-gradient(135deg,#0d0806,#1a0a0a);border:2px solid rgba(229,9,20,0.50);
  border-radius:16px;padding:28px 32px;text-align:center;max-width:380px;margin:0 auto;font-family:Bebas Neue,sans-serif'>
  <div style='font-size:0.60rem;letter-spacing:4px;color:rgba(229,9,20,0.70);margin-bottom:6px'>⚡ FITPLAN PRO</div>
  <div style='font-size:2.2rem;color:#fff;letter-spacing:2px;margin-bottom:4px'>{uname.upper()}</div>
  <div style='font-size:3.5rem;color:#E50914;letter-spacing:2px;line-height:1'>{streak_val}</div>
  <div style='font-size:0.70rem;letter-spacing:3px;color:rgba(255,255,255,0.45);margin-bottom:10px'>DAY STREAK</div>
  <div style='display:flex;justify-content:center;gap:20px'>
    <div><div style='font-size:1.4rem;color:#fff'>{done_count}</div>
         <div style='font-size:0.55rem;letter-spacing:2px;color:rgba(255,255,255,0.35)'>DAYS DONE</div></div>
    <div style='color:rgba(255,255,255,0.15)'>|</div>
    <div><div style='font-size:1.4rem;color:#fff'>{pct_done}%</div>
         <div style='font-size:0.55rem;letter-spacing:2px;color:rgba(255,255,255,0.35)'>COMPLETE</div></div>
    <div style='color:rgba(255,255,255,0.15)'>|</div>
    <div><div style='font-size:1.4rem;color:#fff'>{total_days}</div>
         <div style='font-size:0.55rem;letter-spacing:2px;color:rgba(255,255,255,0.35)'>TOTAL DAYS</div></div>
  </div>
</div>""", unsafe_allow_html=True)
    st.caption("Screenshot this and share on WhatsApp or Instagram! 📱")

# ── PRE-LOAD WORKOUT NOTES ────────────────────────────────────────────────────
if not st.session_state.get("_notes_loaded") and plan_id:
    try:
        from utils.db import get_workout_notes
        for _dn_pre in range(1, min(6, len(sdays)+1)):
            _nk = f"notes_loaded_d{_dn_pre}"
            if not st.session_state.get(_nk):
                for _eidx, _note in get_workout_notes(uname, plan_id, _dn_pre).items():
                    st.session_state[f"note_d{_dn_pre}_e{_eidx}"] = _note
                st.session_state[_nk] = True
        st.session_state._notes_loaded = True
    except Exception: pass

# ── DAY TABS ──────────────────────────────────────────────────────────────────
tab_labels = [f"Day {d.get('day',i+1)}" + (" 😴" if d.get("is_rest_day") else "")
              for i,d in enumerate(sdays)]
# Fix #18,19: Auto-select today's day tab
_today_tab_idx = 0
if sdays:
    _plan_start_dt = date.fromisoformat(st.session_state.get("plan_start", date.today().isoformat()))
    _day_offset = (date.today() - _plan_start_dt).days
    _today_tab_idx = max(0, min(_day_offset, len(sdays)-1))
    if _today_tab_idx > 0:
        st.markdown(
            f"<div style='background:rgba(229,9,20,0.10);border:1px solid rgba(229,9,20,0.30);"
            f"border-radius:10px;padding:8px 16px;margin-bottom:10px;font-size:0.80rem;"
            f"color:rgba(255,255,255,0.75);display:flex;align-items:center;gap:8px'>"
            f"<span style='color:#E50914;font-size:1rem'>&#128197;</span>"
            f"Today is <b style='color:#E50914'>Day {sdays[_today_tab_idx].get('day',_today_tab_idx+1)}"
            f"</b> &mdash; {sdays[_today_tab_idx].get('muscle_group','Workout')} "
            f"&mdash; Scroll to the highlighted tab below</div>",
            unsafe_allow_html=True
        )
tabs = st.tabs(tab_labels)

EX_ICONS   = ["🏋️","💪","🔄","⬆️","🦵","🤸","🏃","🚴","🧗","🥊"]
MEAL_ICONS = {"breakfast":"🌅","lunch":"☀️","dinner":"🌙","snacks":"🍎"}

for tab, day_data in zip(tabs, sdays):
    with tab:
        dn      = day_data.get("day", 1)
        is_rest = day_data.get("is_rest_day", False)
        mg      = day_data.get("muscle_group", "Full Body")

        if is_rest:
            prev_day = next((x for x in sdays if x.get("day") == dn-1), {})
            prev_mg  = prev_day.get("muscle_group", "")
            st.markdown(f"""
            <div class='rest-day'>
              <div style='font-size:3rem;margin-bottom:12px'>😴</div>
              <div style='font-family:Bebas Neue,sans-serif;font-size:2rem;letter-spacing:3px;color:#E50914'>Day {dn} — Rest Day</div>
              <div style='font-size:0.88rem;color:rgba(255,255,255,0.45);margin-top:8px'>Rest and recover. Light stretching, hydration and sleep.</div>
            </div>""", unsafe_allow_html=True)
            rest_sugg_key = f"rest_sugg_d{dn}"
            if not st.session_state.get(rest_sugg_key):
                if st.button(f"💡 Get AI Rest Day Activities", key=f"rest_btn_{dn}"):
                    with st.spinner("Getting suggestions..."):
                        try:
                            from model_api import query_model
                            rp = (f"Give 4 light rest day activities for a {data.get('level','Beginner')} "
                                  f"person, goal: {data.get('goal','Fitness')}."
                                  + (f" Previous workout: {prev_mg}." if prev_mg else "")
                                  + " Format: ACTIVITY: duration — benefit. One per line.")
                            st.session_state[rest_sugg_key] = query_model(rp, max_tokens=200).strip()
                            st.rerun()
                        except Exception as e: st.error(str(e))
            else:
                html_r = ""
                for line in st.session_state[rest_sugg_key].splitlines():
                    line = line.strip()
                    if not line: continue
                    if ":" in line:
                        p = line.split(":",1)
                        html_r += (f"<div style='padding:6px 0;border-bottom:1px solid rgba(229,9,20,0.10)'>"
                                   f"<b style='color:#E50914'>{p[0].strip()}</b>"
                                   f"<span style='color:rgba(255,255,255,0.55)'>: {p[1].strip()}</span></div>")
                    else:
                        html_r += f"<div style='font-size:0.80rem;color:rgba(255,255,255,0.45)'>{line}</div>"
                st.markdown(f"<div style='background:rgba(229,9,20,0.06);border:1px solid rgba(229,9,20,0.18);border-radius:12px;padding:14px 16px;margin-top:10px'>"
                            f"<div style='font-size:0.58rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:rgba(229,9,20,0.75);margin-bottom:10px'>💡 AI REST DAY SUGGESTIONS</div>"
                            f"{html_r}</div>", unsafe_allow_html=True)
            continue

        # Workout day
        left_col, right_col = st.columns([3, 2])

        with left_col:
            pre = day_data.get("pre_stretch", [])
            with st.expander("🔥 Pre-Workout Warm-Up", expanded=False):
                for s in pre:
                    st.markdown(f"<div style='display:flex;gap:10px;align-items:center;padding:6px 0;border-bottom:1px solid rgba(255,255,255,0.05)'>"
                                f"<span style='color:#fbbf24'>🔥</span><div>"
                                f"<div style='font-size:0.88rem;font-weight:600'>{s.get('name','Stretch')}</div>"
                                f"<div style='font-size:0.70rem;color:rgba(255,255,255,0.38)'>⏱ {s.get('duration','30s')}</div></div></div>",
                                unsafe_allow_html=True)
                vurl = pre[0].get("video_url","https://www.youtube.com/embed/R0mMyV5OtcM") if pre else "https://www.youtube.com/embed/R0mMyV5OtcM"
                st.markdown(f"<div style='position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:10px;margin-top:8px'>"
                            f"<iframe src='{vurl}' style='position:absolute;top:0;left:0;width:100%;height:100%;border:none' allowfullscreen></iframe></div>",
                            unsafe_allow_html=True)

            st.markdown(f"<div class='sec-title'>💪 Day {dn} — {mg}</div>", unsafe_allow_html=True)
            exercises = day_data.get("workout", [])
            if not exercises:
                st.markdown("<div style='color:rgba(255,255,255,0.40);padding:20px;text-align:center'>No exercises for this day.</div>", unsafe_allow_html=True)
            else:
                for idx, ex in enumerate(exercises):
                    name_  = ex.get("name",  f"Exercise {idx+1}")
                    sets_  = ex.get("sets",  3)
                    reps_  = ex.get("reps",  "12")
                    rest_  = ex.get("rest",  "60s")
                    timer_ = ex.get("timer", 60)
                    notes_ = ex.get("notes", "Maintain proper form")
                    icon_  = EX_ICONS[idx % len(EX_ICONS)]
                    ck_key = f"ex_d{dn}_{idx}"
                    is_done = st.session_state.get(ck_key, False)
                    yt_url = f"https://www.youtube.com/results?search_query={name_.replace(' ','+')}+exercise+tutorial"

                    with st.expander(f"{icon_} {name_}  —  {sets_} × {reps_}", expanded=False):
                        ec1, ec2 = st.columns([3,2])
                        with ec1:
                            st.markdown(f"""
                            <div class='day-card' style='padding:16px 18px'>
                              <div style='display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap'>
                                <div class='badge b-sets'><span class='badge-num'>{sets_}</span><span class='badge-lbl'>SETS</span></div>
                                <div class='badge b-reps'><span class='badge-num'>{reps_}</span><span class='badge-lbl'>REPS</span></div>
                                <div class='badge b-rest'><span class='badge-num'>{rest_}</span><span class='badge-lbl'>REST</span></div>
                              </div>
                              <div style='font-size:0.75rem;color:rgba(255,255,255,0.55);border-top:1px solid rgba(255,255,255,0.06);padding-top:10px'>
                                <span style='color:rgba(229,9,20,0.70);font-weight:700'>Form tip: </span>{notes_}
                              </div>
                              <a href='{yt_url}' target='_blank' style='display:inline-block;margin-top:10px;font-size:0.68rem;font-weight:700;color:#ff6b6b;text-decoration:none;border:1px solid rgba(255,107,107,0.30);border-radius:6px;padding:3px 10px;background:rgba(255,107,107,0.08)'>▶ Watch Demo</a>
                            </div>""", unsafe_allow_html=True)

                        with ec2:
                            tid = f"d{dn}_e{idx}"
                            st.markdown(f"""
<div style='background:rgba(10,6,4,0.70);border:1.5px solid rgba(229,9,20,0.30);border-radius:14px;padding:18px;text-align:center'>
  <div style='font-size:0.58rem;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:rgba(229,9,20,0.65);margin-bottom:6px'>⏱ TIMER</div>
  <div id='td-{tid}' style='font-family:Bebas Neue,sans-serif;font-size:3.4rem;color:#E50914;letter-spacing:3px;line-height:1'>{timer_}s</div>
  <div style='font-size:0.72rem;color:rgba(255,255,255,0.42);margin:6px 0 12px'>{name_}</div>
  <div style='display:flex;gap:6px;justify-content:center'>
    <button onclick='startT_{tid}()' style='background:linear-gradient(135deg,#E50914,#c0000c);border:none;color:#fff;padding:8px 16px;border-radius:7px;cursor:pointer;font-size:0.78rem;font-weight:700'>▶ Start</button>
    <button onclick='pauseT_{tid}()' style='background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.18);color:rgba(255,255,255,0.65);padding:8px 14px;border-radius:7px;cursor:pointer;font-size:0.78rem;font-weight:700'>⏸</button>
    <button onclick='resetT_{tid}()' style='background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.10);color:rgba(255,255,255,0.40);padding:8px 14px;border-radius:7px;cursor:pointer;font-size:0.78rem;font-weight:700'>↺</button>
  </div>
  <div id='done-{tid}' style='display:none;margin-top:10px;font-family:Bebas Neue,sans-serif;font-size:1.4rem;letter-spacing:2px;color:#22c55e'>✓ TIME'S UP!</div>
</div>
<script>(function(){{const TOTAL={timer_};let t={timer_},run=false,iv=null;
function upd(){{const el=document.getElementById('td-{tid}');if(!el)return;el.textContent=t+'s';
el.style.color=t<=5?'#ef4444':t<=10?'#fbbf24':'#E50914';
if(t<=0){{clearInterval(iv);run=false;el.textContent='✓';el.style.color='#22c55e';
const d=document.getElementById('done-{tid}');if(d)d.style.display='block';
try{{const c=new(window.AudioContext||window.webkitAudioContext)();
[880,1100,1320].forEach((f,i)=>{{const o=c.createOscillator(),g=c.createGain();o.connect(g);g.connect(c.destination);
o.frequency.value=f;g.gain.setValueAtTime(0.3,c.currentTime+i*0.18);
g.gain.exponentialRampToValueAtTime(0.001,c.currentTime+i*0.18+0.3);
o.start(c.currentTime+i*0.18);o.stop(c.currentTime+i*0.18+0.3);}})}}catch(e){{}}}}}}
window.startT_{tid}=function(){{if(run||t<=0)return;run=true;const d=document.getElementById('done-{tid}');if(d)d.style.display='none';iv=setInterval(()=>{{t--;upd();}},1000);}};
window.pauseT_{tid}=function(){{if(!run)return;clearInterval(iv);run=false;}};
window.resetT_{tid}=function(){{clearInterval(iv);run=false;t=TOTAL;const el=document.getElementById('td-{tid}');if(el){{el.textContent=TOTAL+'s';el.style.color='#E50914';}}const d=document.getElementById('done-{tid}');if(d)d.style.display='none';}};
}})();</script>""", unsafe_allow_html=True)

                        # Workout note
                        note_key  = f"note_d{dn}_e{idx}"
                        saved_note = st.session_state.get(note_key, "")
                        new_note   = st.text_area("📝 Note", value=saved_note,
                                                   placeholder="e.g. Felt easy — increase weight next time",
                                                   key=f"note_input_d{dn}_e{idx}", height=68,
                                                   label_visibility="collapsed")
                        if new_note != saved_note:
                            st.session_state[note_key] = new_note
                            if plan_id:
                                try:
                                    from utils.db import save_workout_note
                                    save_workout_note(uname, plan_id, dn, idx, new_note)
                                except Exception: pass

                        # Checkbox
                        if is_done:
                            st.markdown(f"<div style='background:rgba(34,197,94,0.12);border:1px solid rgba(34,197,94,0.35);border-radius:8px;padding:8px 14px;font-size:0.82rem;color:#4ade80;font-weight:700'>✅ {name_} — Completed</div>", unsafe_allow_html=True)
                        else:
                            if st.checkbox(f"✅ Mark {name_} Done", value=False, key=ck_key+"_cb"):
                                st.session_state[ck_key] = True
                                if plan_id:
                                    try:
                                        from utils.db import save_progress
                                        wc = {f"ex_{i}": st.session_state.get(f"ex_d{dn}_{i}", False) for i in range(len(exercises))}
                                        dc = {m: st.session_state.get(f"meal_d{dn}_{m}", False) for m in ["breakfast","lunch","dinner","snacks"]}
                                        save_progress(uname, plan_id, dn, wc, dc)
                                    except Exception: pass
                                st.session_state["_needs_rerun"] = True

            # ── Feature #3: RPE Rating ────────────────────────────────────
            rpe_key = f"rpe_d{dn}"
            current_rpe = st.session_state.get(rpe_key, 0)
            st.markdown(
                "<div style='background:rgba(10,6,4,0.70);border:1px solid rgba(255,255,255,0.12);"
                "border-radius:12px;padding:14px 18px;margin:12px 0;backdrop-filter:blur(8px)'>"
                "<div style='font-size:0.60rem;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;"
                "color:rgba(229,9,20,0.75);margin-bottom:8px'>&#9889; Rate Workout Intensity (RPE 1-10)</div>"
                "<div style='display:flex;gap:6px;flex-wrap:wrap;margin-bottom:6px'>",
                unsafe_allow_html=True
            )
            rpe_cols = st.columns(10)
            for _ri in range(1, 11):
                rpe_label = str(_ri)
                rpe_color = ("#22c55e" if _ri <= 3 else "#fbbf24" if _ri <= 6 else "#f97316" if _ri <= 8 else "#ef4444")
                is_sel = (current_rpe == _ri)
                with rpe_cols[_ri-1]:
                    if st.button(
                        rpe_label,
                        key=f"rpe_{dn}_{_ri}",
                        use_container_width=True,
                        help=["","Very Easy","Easy","Moderate","Somewhat Hard","Hard","Hard","Very Hard","Very Hard","Max Effort","Max Effort"][_ri]
                    ):
                        st.session_state[rpe_key] = _ri
                        try:
                            from utils.db import save_user_setting
                            save_user_setting(uname, f"rpe_d{dn}", str(_ri))
                        except Exception: pass
                        st.toast(f"⚡ RPE {_ri} saved for Day {dn}!", icon="💪")
                        st.rerun()
            if current_rpe > 0:
                rpe_desc = ["","Very Easy 😌","Easy 🙂","Moderate 😊","Somewhat Hard 😤","Hard 😰","Hard 😰","Very Hard 🥵","Very Hard 🥵","Max Effort 😵","Max Effort 💀"][current_rpe]
                rpe_c = "#22c55e" if current_rpe<=3 else "#fbbf24" if current_rpe<=6 else "#f97316" if current_rpe<=8 else "#ef4444"
                st.markdown(
                    f"<div style='margin-top:6px;font-size:0.78rem;font-weight:600;color:{rpe_c}'>"
                    f"Selected: RPE {current_rpe} — {rpe_desc}</div>",
                    unsafe_allow_html=True
                )
            st.markdown("</div>", unsafe_allow_html=True)

            post = day_data.get("post_stretch", [])
            with st.expander("🧊 Post-Workout Cool-Down", expanded=False):
                for s in post:
                    st.markdown(f"<div style='display:flex;gap:10px;align-items:center;padding:6px 0;border-bottom:1px solid rgba(255,255,255,0.05)'>"
                                f"<span style='color:#22c55e'>🧊</span><div>"
                                f"<div style='font-size:0.88rem;font-weight:600'>{s.get('name','Stretch')}</div>"
                                f"<div style='font-size:0.70rem;color:rgba(255,255,255,0.38)'>⏱ {s.get('duration','40s')}</div></div></div>",
                                unsafe_allow_html=True)
                vurl2 = post[0].get("video_url","https://www.youtube.com/embed/Qyd_guFDMh4") if post else "https://www.youtube.com/embed/Qyd_guFDMh4"
                st.markdown(f"<div style='position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:10px;margin-top:8px'>"
                            f"<iframe src='{vurl2}' style='position:absolute;top:0;left:0;width:100%;height:100%;border:none' allowfullscreen></iframe></div>",
                            unsafe_allow_html=True)

        with right_col:
            dietary   = day_data.get("dietary", {})
            diet_type = st.session_state.get("dietary_type","veg")
            st.markdown(f"""
            <div style='background:rgba(10,20,12,0.60);border:1px solid rgba(34,197,94,0.20);
              border-radius:16px;padding:20px 22px;position:relative;overflow:hidden'>
              <div style='position:absolute;top:0;left:0;right:0;height:1.5px;
                background:linear-gradient(90deg,transparent,rgba(34,197,94,0.50),transparent)'></div>
              <div style='font-size:0.58rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;
                color:rgba(34,197,94,0.75);margin-bottom:16px;display:flex;align-items:center;gap:6px'>
                <span style='width:14px;height:1.5px;background:#22c55e;display:block'></span>
                🥗 Day {dn} Diet Plan
                <span style='margin-left:auto;font-size:0.60rem;color:rgba(34,197,94,0.55)'>
                  {'🌿 Veg' if diet_type=='veg' else '🍗 Non-Veg'}
                </span>
              </div>
            """, unsafe_allow_html=True)
            for meal, desc in dietary.items():
                if not desc: continue
                icon  = MEAL_ICONS.get(meal,"🍽️")
                ck    = f"meal_d{dn}_{meal}"
                done  = st.session_state.get(ck, False)
                strike = "text-decoration:line-through;opacity:0.50;" if done else ""
                st.markdown(f"<div class='meal-card'><div class='meal-lbl'>{icon} {meal.upper()}</div>"
                            f"<div class='meal-txt' style='{strike}'>{desc}</div></div>", unsafe_allow_html=True)
                if st.checkbox(f"✅ {meal.title()} done", value=done, key=ck+"_cb"):
                    if not done:
                        st.session_state[ck] = True
                        if plan_id:
                            try:
                                from utils.db import save_progress
                                wc_ = {f"ex_{i}": st.session_state.get(f"ex_d{dn}_{i}",False) for i in range(len(exercises if not is_rest else []))}
                                dc_ = {m2: st.session_state.get(f"meal_d{dn}_{m2}",False) for m2 in ["breakfast","lunch","dinner","snacks"]}
                                save_progress(uname, plan_id, dn, wc_, dc_)
                            except Exception: pass
                        st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.pop("_needs_rerun", False):
    st.rerun()