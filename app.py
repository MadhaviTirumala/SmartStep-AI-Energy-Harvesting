import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from energy_model import predict_energy

st.title("SmartStep AI Energy Dashboard")

footfall_today = np.random.randint(500, 2000)
energy_generated = round(footfall_today * 0.02, 2)

st.metric("Total Footfall Today", footfall_today)
st.metric("Energy Generated (kWh)", energy_generated)

st.subheader("Predict Energy from Footfall")
input_footfall = st.slider("Select Footfall", 100, 3000, 1000)

predicted_energy = predict_energy(input_footfall)
st.success(f"Predicted Energy: {predicted_energy} kWh")

st.subheader("Footfall Trend")
days = np.arange(1, 31)
random_footfall = np.random.randint(200, 1500, 30)

plt.plot(days, random_footfall)
plt.xlabel("Day")
plt.ylabel("Footfall")
st.pyplot(plt)