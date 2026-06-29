import streamlit as st
import pandas as pd
import joblib

st.title("🚧 Soil Slope Stability Risk Assessment")
# --- About the Model Section ---

    # --- About the Model Section ---
with st.expander("ℹ️ About the Model & Engineering Physics"):
    st.markdown(r"""
    ### 📐 Governing Equation
    This application utilizes a data-driven approach trained on a physics-informed dataset. 
    The underlying synthetic training data was generated using the classical **Limit Equilibrium Method** for infinite slopes:
    """)
    
    # Renders the mathematical formula beautifully
    st.latex(r"FoS = \frac{c}{\gamma H} + \frac{\tan(\phi)}{\tan(\beta)}")
    
    st.markdown(r"""
    **Parameter Legend:**
    * **$c$** = Soil Cohesion (kPa) — *Resists shearing along the failure surface.*
    * **$\phi$** = Internal Friction Angle (degrees) — *The frictional resistance between soil particles.*
    * **$\beta$** = Slope Angle (degrees) — *The steepness of the slope face.*
    * **$H$** = Slope Height (m) — *The vertical height of the soil mass.*
    * **$\gamma$** = Soil Unit Weight (kN/m³) — *The weight density of the soil material.*
    
    ---

    ### 📊 Factor of Safety ($FoS$) Interpretation Ranges
    In geotechnical engineering practice, the calculated or predicted stability score falls into these distinct safety thresholds:
    """)

    # Displaying a clean, readable reference table for the user
    st.table({
        "FoS Range": ["FoS < 1.0", "1.0 <= FoS < 1.3", "1.3 <= FoS < 1.5", "FoS >= 1.5"],
        "Stability Status": ["🔴 Unstable (Active Failure)", "🟡 Marginally Stable / Critical", "🟢 Acceptable (Temporary Slopes)", "🟢 Safe (Permanent Engineering Design)"],
        "Engineering Action Required": ["Immediate remediation / structural retaining wall needed.", "High risk. Detailed field investigation and monitoring required.", "Suitable for low-risk or short-term excavation projects.", "Standard target threshold met for long-term civil works."]
    })

    st.markdown(r"""
    ---
    
    ### 🤖 Machine Learning Pipeline (MLOps)
    Instead of calculating the formula directly in the app, this dashboard serves a live **Random Forest Regressor** model:
    1. **Data Generation:** 1,000 synthetic soil profiles were generated using uniform distributions across practical engineering ranges.
    2. **Training:** A 50-tree Random Forest was trained using `scikit-learn` to map the non-linear interactions between parameters and the target Factor of Safety ($FoS$).
    3. **Serialization:** The trained "brain" was frozen into a binary `slope_stability_model.pkl` file using `joblib`.
    4. **Deployment:** Streamlit extracts the model from the `.pkl` file via `joblib.load()` to output real-time predictions instantly when you adjust the sidebar sliders.
    """)
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
