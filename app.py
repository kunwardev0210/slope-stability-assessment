import streamlit as st
import pandas as pd
import joblib

st.title("🚧 Soil Slope Stability Risk Assessment")
st.write("Move the sliders to predict the Factor of Safety (FoS) in real-time.")

# Load the saved model file
model = joblib.load('slope_stability_model.pkl')

# 5 User Sliders on the Sidebar
cohesion = st.sidebar.slider("Soil Cohesion (c) [kPa]", 10.0, 50.0, 25.0)
friction_angle = st.sidebar.slider("Internal Friction Angle (φ) [deg]", 15.0, 40.0, 28.0)
slope_angle = st.sidebar.slider("Slope Angle (β) [deg]", 18.0, 55.0, 35.0)
slope_height = st.sidebar.slider("Slope Height (H) [m]", 4.0, 30.0, 12.0)
unit_weight = st.sidebar.slider("Soil Unit Weight (γ) [kN/m³]", 16.0, 22.0, 18.0)

# Bundle sliders together matching the exact names used in your notebook data
input_features = pd.DataFrame({
    'cohesion_kPa': [cohesion],
    'friction_angle_deg': [friction_angle],
    'slope_angle_deg': [slope_angle],
    'slope_height_m': [slope_height],
    'unit_weight_kNm3': [unit_weight]
})

# Run prediction
prediction = model.predict(input_features)[0]

# Display the result beautifully
st.metric(label="Predicted Factor of Safety (FoS)", value=f"{prediction:.3f}")

if prediction > 1.5:
    st.success("🟢 STATUS: STABLE")
elif 1.0 <= prediction <= 1.5:
    st.warning("🟡 STATUS: MARGINALLY STABLE")
else:
    st.error("🔴 STATUS: UNSTABLE (High Risk of Failure)")
