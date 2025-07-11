import random

def generate_glitch_explanation(topic):
    glitches = [
        f"⚠️ Simulation Bug in '{topic}': Backprop loop collapsed into recursion vortex.",
        f"🧠 Neural residue from previous training phase has leaked into {topic} weights.",
        f"⛔ {topic} overflow error: Gradient exploded like a cosmic ray.",
        f"💀 Conceptual deadlock in {topic}. Synapse stuck in an infinite update cycle.",
        f"🚨 {topic} system malfunction: Output diverges when confidence > 0.95.",
    ]

    explanation = {
        "title": f"🧠 Target: {topic}",
        "glitch": random.choice(glitches),
        "deep_story": (
            f"{topic} behaves like a dream — full of hidden signals and chaos. "
            f"It needs structured input and patient tweaking to behave. "
            f"Remember, it’s not magic. It’s just layered logic pretending to be smart."
        ),
        "fix_suggestion": (
            "🛠️ Fix: Simplify the problem. Visualize it. "
            "Use diagrams, animations, and small steps. Don't debug the universe."
        )
    }
    return explanation
