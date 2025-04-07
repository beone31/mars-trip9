
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import time

st.set_page_config(page_title="Earth to Mars Journey", layout="wide")
st.title("🪐 Earth to Mars: 3-Minute Journey")
st.markdown("A narrated educational animation featuring rocket sounds and visuals of outer space.")

# Load and play rocket + ambient audio
base_path = os.path.dirname(__file__)
audio_path = os.path.join(os.path.dirname(__file__), "assets", "rocket_ambience.mp3")
with open(audio_path, "rb") as audio_file:
    st.audio(audio_file.read(), format="audio/mp3")

# Load images
earth = mpimg.imread(os.path.join(os.path.dirname(__file__), "assets", "earth.png"))
mars = mpimg.imread(os.path.join(os.path.dirname(__file__), "assets", "mars.png"))
rocket = mpimg.imread(os.path.join(os.path.dirname(__file__), "assets", "rocket.png"))

# Narration segments
narration = {
    0: "Liftoff! The rocket launches from Earth and begins its interplanetary voyage.",
    20: "We've escaped Earth's atmosphere and are now in outer space.",
    40: "Our spacecraft is halfway through the journey to Mars.",
    70: "We're approaching the Martian orbit. Prepare for orbital insertion.",
    90: "Touchdown confirmed. Welcome to Mars!"
}

# Animation setup
fig, ax = plt.subplots(figsize=(10, 4))
earth_x, mars_x = 1, 9
frames = 100
spacecraft_path = np.linspace(earth_x, mars_x, frames)
spacecraft_y = np.sin(np.linspace(0, np.pi, frames)) * 0.5

canvas = st.empty()
narration_display = st.empty()

for i in range(frames):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 1)
    ax.set_facecolor("black")
    ax.imshow(earth, extent=[earth_x-0.5, earth_x+0.5, -0.5, 0.5])
    ax.imshow(mars, extent=[mars_x-0.5, mars_x+0.5, -0.5, 0.5])
    ax.imshow(rocket, extent=[spacecraft_path[i]-0.2, spacecraft_path[i]+0.2,
                              spacecraft_y[i]-0.4, spacecraft_y[i]+0.4])
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    canvas.pyplot(fig)

    if i in narration:
        narration_display.markdown(f"### 🎙️ {narration[i]}")
    time.sleep(1.8)  # ~180 seconds total
