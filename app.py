# app.py

import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="SkillGlitch AI", layout="centered")

st.title("🧠 SkillGlitch AI – Skill DNA Mapper")
st.caption("Decode your skills. Learn through simulation bugs.")

# --- Skill Input Section ---
st.header("📥 Input Your Skills")

strong_skills = st.text_input(
    "🔰 List 3 topics you're STRONG at (comma-separated):",
    placeholder="e.g. Artificial Intelligence, Prompt Engineering, Image Generation")

weak_skills = st.text_input(
    "⚠️ List 3 topics you find WEAK or CONFUSING (comma-separated):",
    placeholder="e.g. Deep Learning, Machine Learning, Logic Building")

confidence = st.slider("🧭 On a scale of 1–10, how confident are you overall in tech?", 1, 10, 7)

user_name = st.text_input("🙋 Your Name:", value="Thejo Karthikeya")

# --- On Submit ---
if st.button("🔍 Generate My Skill DNA"):
    strong_list = [s.strip() for s in strong_skills.split(",") if s.strip()]
    weak_list = [w.strip() for w in weak_skills.split(",") if w.strip()]

    if len(strong_list) != 3 or len(weak_list) != 3:
        st.error("⚠️ Please enter exactly 3 strong and 3 weak topics.")
    else:
        skill_profile = {
            "name": user_name,
            "timestamp": str(datetime.now()),
            "strong_skills": strong_list,
            "weak_skills": weak_list,
            "confidence_level": confidence,
            "learning_style": "Simulation-driven storytelling with visual aids",
            "recommendations": {
                "priority_focus": weak_list[0],
                "style_suggestion": "Use glitch-based analogies + code story debugging"
            }
        }

        st.success("✅ Skill DNA Profile Generated!")
        st.subheader("🧬 Your Skill DNA")
        st.json(skill_profile)

        # Save to file (optional)
        with open("skill_dna.json", "w") as f:
            json.dump(skill_profile, f, indent=2)

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


