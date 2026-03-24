# -*- coding: utf-8 -*-
import streamlit as st
import os, sys
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from auth_token import logout
from bg_utils import apply_bg

st.set_page_config(page_title="FitPlan Pro - Flexible Diet", page_icon="🌿",
                   layout="wide", initial_sidebar_state="collapsed")

if not st.session_state.get("logged_in"):
    st.switch_page("app.py")
if "user_data" not in st.session_state:
    st.switch_page("pages/1_Profile.py")

uname     = st.session_state.get("username", "Athlete")
data      = st.session_state.user_data
sdays     = st.session_state.get("structured_days", [])
plan_id   = st.session_state.get("plan_id", "")
today_str = date.today().isoformat()

NUTRITION_TIPS = [
    "&#128167; Drink 2.5-3 litres of water daily",
    "&#127807; Fill half your plate with vegetables",
    "&#127829; Alternate veg &amp; non-veg days for variety",
    "&#9201; Eat every 3-4 hours to keep metabolism active",
    "&#128138; Limit processed foods and refined carbs",
    "&#129385; Post-workout: lean protein within 30 mins",
    "&#127822; Snack on fruits, nuts, and yoghurt",
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow+Condensed:wght@700;800;900&family=DM+Sans:opsz,wght@9..40,400;9..40,600;9..40,700&display=swap');

#MainMenu, footer, header,
[data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stSidebarNav"], [data-testid="collapsedControl"],
section[data-testid="stSidebar"], button[kind="header"] { display:none!important; }

html,body,.stApp { background-color:transparent!important; color:#fff!important; font-family:'DM Sans',sans-serif!important; }
[data-testid="stAppViewContainer"]>section>div.block-container {
  max-width:1200px!important; margin:0 auto!important; padding:0 32px 80px!important; background:transparent!important; }
[data-testid="stWidgetLabel"],[data-testid="stWidgetLabel"] p { color:rgba(255,255,255,0.80)!important; }

.stButton>button { background:linear-gradient(135deg,#ca8a04,#a16207)!important;
  border:none!important; color:#fff!important; border-radius:8px!important;
  font-family:'DM Sans',sans-serif!important; font-size:0.85rem!important; font-weight:700!important;
  text-transform:uppercase!important; letter-spacing:0.5px!important;
  box-shadow:0 4px 18px rgba(202,138,4,0.40)!important; transition:all 0.20s!important; }
.stButton>button:hover { transform:translateY(-2px)!important; box-shadow:0 6px 28px rgba(202,138,4,0.65)!important; }

.stTabs [data-baseweb="tab-list"] { background:rgba(20,35,8,0.80)!important; border-radius:10px!important;
  padding:4px!important; border:1px solid rgba(250,204,21,0.22)!important; }
.stTabs [data-baseweb="tab"] { background:transparent!important; color:rgba(255,255,255,0.50)!important;
  border-radius:7px!important; font-size:0.75rem!important; font-weight:600!important; border:none!important; padding:8px 14px!important; }
.stTabs [aria-selected="true"] { background:linear-gradient(135deg,#ca8a04,#a16207)!important;
  color:#fff!important; box-shadow:0 3px 12px rgba(202,138,4,0.50)!important; }
.stCheckbox>label { color:#fff!important; }

div[data-testid="stHorizontalBlock"]:first-of-type div[data-testid="stButton"]>button {
  background:rgba(202,138,4,0.20)!important; border:2px solid #ca8a04!important;
  color:#fff!important; border-radius:8px!important; letter-spacing:1.5px!important;
  font-size:0.68rem!important; font-weight:700!important; padding:7px 8px!important;
  height:38px!important; min-height:38px!important; text-transform:uppercase!important;
  box-shadow:0 2px 10px rgba(202,138,4,0.25)!important; transition:all 0.15s ease!important; }
div[data-testid="stHorizontalBlock"]:first-of-type div[data-testid="stButton"]>button:hover {
  background:rgba(202,138,4,0.48)!important; transform:translateY(-1px)!important; }
div[data-testid="stHorizontalBlock"]:first-of-type div[data-testid="stButton"]:last-child>button {
  background:rgba(229,9,20,0.30)!important; border:2px solid #E50914!important; }

.nav-logo-txt { font-family:'Bebas Neue',sans-serif; font-size:1.5rem; letter-spacing:5px;
  color:#facc15; text-shadow:0 0 20px rgba(250,204,21,0.55); line-height:1; }
.meal-card { background:rgba(12,25,5,0.90); border:1.5px solid rgba(250,204,21,0.25);
  border-radius:12px; padding:16px 20px; margin-bottom:12px; position:relative; overflow:hidden; }
.meal-card::before { content:''; position:absolute; top:0; left:0; right:0; height:2px;
  background:linear-gradient(90deg,transparent,rgba(250,204,21,0.55),transparent); }
.meal-label { font-size:0.58rem; font-weight:700; letter-spacing:2.5px; text-transform:uppercase;
  color:rgba(250,204,21,0.90); margin-bottom:8px; display:flex; align-items:center; gap:6px; }
.meal-text { font-size:0.90rem; color:rgba(255,255,255,0.88); line-height:1.65; }
.tip-card { background:rgba(12,25,5,0.75); border:1px solid rgba(250,204,21,0.20);
  border-radius:10px; padding:10px 14px; margin-bottom:8px; font-size:0.82rem;
  color:rgba(255,255,255,0.75); display:flex; align-items:center; gap:8px; }
.progress-bar-bg { height:6px; background:rgba(255,255,255,0.10); border-radius:3px; overflow:hidden; margin-top:6px; }
.progress-bar-fill { height:100%; background:linear-gradient(90deg,#facc15,#ca8a04); border-radius:3px; }

.stNumberInput>div>div>input, .stTextInput>div>div>input {
  background:rgba(255,255,255,0.08)!important; border:1.5px solid rgba(255,255,255,0.22)!important;
  color:#fff!important; border-radius:14px!important; backdrop-filter:blur(12px)!important;
  box-shadow:0 2px 12px rgba(0,0,0,0.30)!important; }
[data-baseweb="select"]>div { background:rgba(255,255,255,0.08)!important;
  border:1.5px solid rgba(255,255,255,0.22)!important; border-radius:14px!important;
  backdrop-filter:blur(12px)!important; color:#fff!important; }
[data-baseweb="select"] span,[data-baseweb="select"] div { color:#fff!important; }
[data-baseweb="popover"] [role="option"] { background:rgba(5,5,5,0.96)!important; color:#fff!important; }
</style>
""", unsafe_allow_html=True)

apply_bg(
    "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?fm=jpg&w=1600&q=80&fit=crop",
    overlay="rgba(20,35,8,0.50)"
)

# NAV
st.markdown("<div style='padding:8px 0;margin-bottom:20px'>", unsafe_allow_html=True)
_n = st.columns([1.6,1,1,1,1,1,1,1.2])
with _n[0]: st.markdown("<div class='nav-logo-txt'>&#127807;&#127829; FITPLAN PRO</div>", unsafe_allow_html=True)
with _n[1]:
    if st.button("Dashboard", key="bd_db", use_container_width=True): st.switch_page("pages/2_Dashboard.py")
with _n[2]:
    if st.button("Profile",   key="bd_pr", use_container_width=True): st.switch_page("pages/1_Profile.py")
with _n[3]:
    if st.button("Diet Menu", key="bd_dm", use_container_width=True): st.switch_page("pages/4_Diet_Plan.py")
with _n[4]:
    if st.button("Workout",   key="bd_wp", use_container_width=True): st.switch_page("pages/3_Workout_Plan.py")
with _n[5]:
    if st.button("AI Coach",  key="bd_ai", use_container_width=True):
        try: st.switch_page("pages/5_ai_coach.py")
        except Exception as e: st.warning(str(e))
with _n[6]:
    if st.button("Records",   key="bd_rc", use_container_width=True):
        try: st.switch_page("pages/6_records.py")
        except Exception as e: st.warning(str(e))
with _n[7]:
    if st.button("Sign Out",  key="bd_so", use_container_width=True):
        logout(uname)
        for _k in ["logged_in","username","auth_token","user_data","workout_plan",
                   "structured_days","dietary_type","full_plan_data","plan_id","plan_start",
                   "plan_duration","plan_for","force_regen","tracking","_plan_checked",
                   "_db_loaded_dash","_auto_redirect","_diet_chosen","_needs_rerun",
                   "_db_streak","edit_profile_mode","_login_db_err","_notes_loaded"]:
            st.session_state.pop(_k, None)
        st.switch_page("app.py")
st.markdown("</div>", unsafe_allow_html=True)

# HERO
uname_up = uname.upper()
st.markdown(
    "<div style='background:linear-gradient(135deg,rgba(20,40,8,0.92),rgba(40,25,5,0.82) 50%,rgba(15,30,5,0.94));"
    "border:1.5px solid rgba(250,204,21,0.35);border-radius:20px;padding:36px 44px;margin-bottom:28px;"
    "position:relative;overflow:hidden'>"
    "<div style='position:absolute;top:0;left:0;right:0;height:2px;"
    "background:linear-gradient(90deg,transparent,#facc15,#22c55e,#f97316,transparent)'></div>"
    "<div style='position:absolute;top:16px;right:24px;font-size:0.72rem;font-weight:700;"
    "letter-spacing:2px;color:rgba(250,204,21,0.80);background:rgba(250,204,21,0.10);"
    "border:1px solid rgba(250,204,21,0.28);border-radius:20px;padding:4px 14px'>&#127807;&#127829; Flexible</div>"
    "<div style='font-size:0.62rem;font-weight:700;letter-spacing:4px;text-transform:uppercase;"
    "color:rgba(250,204,21,0.80);margin-bottom:10px'>Personalised Nutrition Plan</div>"
    "<div style='font-family:Barlow Condensed,sans-serif;font-size:clamp(2rem,5vw,3.6rem);"
    "font-weight:900;text-transform:uppercase;color:#fff;line-height:1;margin-bottom:14px'>"
    + uname_up + "'s <span style='color:#facc15'>Diet Plan</span></div>"
    "<div style='display:flex;gap:12px;flex-wrap:wrap;margin-bottom:16px'>"
    "<span style='background:rgba(34,197,94,0.12);border:1px solid rgba(34,197,94,0.32);"
    "border-radius:20px;padding:4px 12px;font-size:0.76rem;font-weight:600;color:#22c55e'>&#127807; Veg options</span>"
    "<span style='background:rgba(249,115,22,0.12);border:1px solid rgba(249,115,22,0.32);"
    "border-radius:20px;padding:4px 12px;font-size:0.76rem;font-weight:600;color:#f97316'>&#127829; Non-veg options</span>"
    "<span style='font-size:0.82rem;color:rgba(255,255,255,0.45);align-self:center'>"
    "Goal: " + data.get("goal","Fitness") + "</span></div></div>",
    unsafe_allow_html=True
)

if not sdays:
    st.warning("No plan found. Please generate your plan from the Profile page.")
    if st.button("Go to Profile"): st.switch_page("pages/1_Profile.py")
    st.stop()

tab_labels = ["Day " + str(d.get("day",i+1)) + (" &#128564;" if d.get("is_rest_day") else "") for i,d in enumerate(sdays)]
tabs = st.tabs(tab_labels)
MEAL_ICONS = {"breakfast":"&#127773;","lunch":"&#9728;&#65039;","dinner":"&#127769;","snacks":"&#127822;"}

for tab, day_data in zip(tabs, sdays):
    with tab:
        dn          = day_data.get("day", 1)
        dietary     = day_data.get("dietary", {})
        is_rest     = day_data.get("is_rest_day", False)
        mg          = day_data.get("muscle_group", "Full Body")
        total_meals = len([m for m,v in dietary.items() if v])
        done_meals  = sum(1 for m in dietary if st.session_state.get("meal_d"+str(dn)+"_"+m, False))
        pct_meals   = int(done_meals / max(total_meals,1) * 100)

        col_hdr, col_pct = st.columns([4,1])
        with col_hdr:
            tag = "REST DAY" if is_rest else ("DAILY NUTRITION — " + mg.upper())
            st.markdown("<div style='font-size:0.62rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;"
                        "color:rgba(250,204,21,0.80);margin-bottom:6px'>" + tag + "</div>", unsafe_allow_html=True)
        with col_pct:
            st.markdown("<div style='text-align:right;font-size:0.75rem;font-weight:700;"
                        "color:rgba(250,204,21,0.80);padding-top:4px'>"
                        + str(done_meals) + "/" + str(total_meals) + " &middot; " + str(pct_meals) + "%</div>",
                        unsafe_allow_html=True)

        left_col, right_col = st.columns([3,2])
        with left_col:
            if not dietary:
                st.markdown("<div style='color:rgba(255,255,255,0.35);font-size:0.82rem;"
                            "padding:20px 0;text-align:center'>No meal data for this day.</div>", unsafe_allow_html=True)
            else:
                for meal, desc in dietary.items():
                    if not desc: continue
                    icon  = MEAL_ICONS.get(meal, "&#127869;&#65039;")
                    ck    = "meal_d" + str(dn) + "_" + meal
                    done  = st.session_state.get(ck, False)
                    strike = "text-decoration:line-through;opacity:0.40;" if done else ""
                    check  = " <span style='color:#facc15'>&#10003;</span>" if done else ""
                    st.markdown(
                        "<div class='meal-card'><div class='meal-label'>"
                        "<span>" + icon + "</span><span>" + meal.upper() + "</span>" + check + "</div>"
                        "<div class='meal-text' style='" + strike + "'>" + str(desc) + "</div></div>",
                        unsafe_allow_html=True)
                    if st.checkbox("Mark as done", value=done, key=ck+"_cb"):
                        if not done:
                            st.session_state[ck] = True
                            if plan_id:
                                try:
                                    from utils.db import save_progress
                                    dc_ = {m2: st.session_state.get("meal_d"+str(dn)+"_"+m2,False)
                                           for m2 in ["breakfast","lunch","dinner","snacks"]}
                                    save_progress(uname, plan_id, dn, {}, dc_)
                                except Exception: pass
                            st.rerun()

        with right_col:
            st.markdown(
                "<div style='background:rgba(12,25,5,0.75);border:1px solid rgba(250,204,21,0.20);"
                "border-radius:12px;padding:16px 18px;margin-bottom:14px'>"
                "<div style='font-size:0.60rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;"
                "color:rgba(250,204,21,0.75);margin-bottom:10px'>Today's Progress</div>"
                "<div style='display:flex;justify-content:space-between;margin-bottom:4px'>"
                "<span style='font-size:0.78rem;color:rgba(255,255,255,0.55)'>Meals completed</span>"
                "<span style='font-size:0.78rem;font-weight:700;color:#facc15'>"
                + str(done_meals) + " / " + str(total_meals) + "</span></div>"
                "<div class='progress-bar-bg'><div class='progress-bar-fill' style='width:"
                + str(pct_meals) + "%'></div></div></div>",
                unsafe_allow_html=True)
            st.markdown(
                "<div style='background:rgba(12,25,5,0.75);border:1px solid rgba(250,204,21,0.20);"
                "border-radius:12px;padding:16px 18px'>"
                "<div style='font-size:0.60rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;"
                "color:rgba(250,204,21,0.75);margin-bottom:10px'>&#128161; Nutrition Tips</div>",
                unsafe_allow_html=True)
            for tip in NUTRITION_TIPS[:5]:
                st.markdown("<div class='tip-card'>" + tip + "</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)