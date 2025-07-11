import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="SkillGlitch AI", page_icon="🧠", layout="centered")

# === HEADER ===
st.title("🧠 SkillGlitch AI – Skill DNA Mapper")
st.caption("Decode your skills. Learn through simulation bugs.")

# === SKILL INPUT UI ===
st.header("📥 Input Your Skills")

strong_skills = st.text_input(
    "📚 List 3 topics you're STRONG at (comma-separated):",
    placeholder="e.g. Artificial Intelligence, Prompt Engineering, Image Generation"
).split(",")

weak_skills = st.text_input(
    "⚠️ List 3 topics you find WEAK or CONFUSING (comma-separated):",
    placeholder="e.g. Deep Learning, Machine Learning, Logic Building"
).split(",")

confidence_level = st.slider(
    "⏱️ On a scale of 1–10, how confident are you overall in tech?",
    min_value=1, max_value=10, value=5
)

if st.button("🧬 Generate My Skill DNA"):
    name = "Thejo Karthikeya"  # Or make this a user input later

    learning_style = "Simulation-driven storytelling with visual aids"

    Skill_profile = {
        "name": name,
        "timestamp": str(datetime.now()),
        "strong_skills": [s.strip() for s in strong_skills if s.strip()],
        "weak_skills": [w.strip() for w in weak_skills if w.strip()],
        "confidence_level": confidence_level,
        "learning_style": learning_style,
        "recommendations": {
            "priority_focus": weak_skills[0].strip() if weak_skills else "",
            "style_suggestion": "Use glitch-based analogies + code story debugging"
        }
    }

    st.success("✅ Skill DNA Profile Generated!")
    st.json(Skill_profile, indent=2)

    # ✅ This line is necessary for Glitch Explainer to work!
    st.session_state["Skill_DNA"] = Skill_profile

# === DAY 3 – Glitch Explainer Engine ===
st.markdown("---")
st.header("👾 Glitch Explainer Engine")

st.caption("Pick a confusing topic. Let AI break it down like a simulation bug.")

if "Skill_DNA" in st.session_state:
    weak_list = st.session_state["Skill_DNA"]["weak_skills"]

    selected_topic = st.selectbox("🧩 Choose a weak topic:", weak_list)

    if st.button("⚡ Generate Glitch Explanation"):
        from glitch_engine import generate_glitch_explanation
        glitch = generate_glitch_explanation(selected_topic)

        st.subheader(glitch["title"])
        st.markdown(f"```glitch\n{glitch['glitch']}\n```")
        st.write(f"📖 **Understanding:** {glitch['deep_story']}")
        st.write(f"✅ {glitch['fix_suggestion']}")
else:
    st.warning("⚠️ Please generate your Skill DNA first to see glitch topics.")
