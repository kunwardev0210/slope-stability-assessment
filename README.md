# ⛰️ Production-Grade Slope Stability Assessment Dashboard

A high-performance, responsive civil engineering and machine learning web application that predicts the **Factor of Safety (FoS)** for soil profiles in real-time. This project features a **physics-informed data science architecture** that replaces iterative, computationally heavy limit equilibrium calculations with an instant, low-latency machine learning inference layer.

🔗 **Live Deployment URL:** [Streamlit Community Cloud](https://kunwardev0210-slope-stability-assessment-app-lud3j1.streamlit.app/) 

---

## 🚀 Key Features

* **Physics-Informed Synthetic Dataset:** Evaluated across 1,000 unique geotechnical configurations generated via classical deterministic Limit Equilibrium Method equations to enforce realistic training boundaries.
* **Low-Latency Inference Pipeline:** Completely decoupled from heavy mathematical runtime arithmetic; uses an unpickled machine learning brain to serve stable predictions in under 10 milliseconds.
* **Dynamic Geotechnical UI:** Engineered with interactive sidebar controls that map real-world physical soil constraints directly into the multidimensional prediction matrix.
* **Academic-Grounded Transparency:** Features a dedicated on-screen expander containing LaTeX formatting equations and standardized engineering design threshold matrices.

---

## 📐 Governing Physics Framework

The core synthetic dataset mimics an infinite slope scenario under critical boundary conditions. The underlying mathematical model evaluating the failure plane is governed by the classical physics equation:

$$FoS = \frac{c}{\gamma H} + \frac{\tan(\phi)}{\tan(\beta)}$$

### Engineering Parameters & Feature Mapping:
* **$c$ (Soil Cohesion) [kPa]:** The intrinsic shearing resistance holding the soil mass intact along a prospective failure surface.
* **$\phi$ (Internal Friction Angle) [degrees]:** The interlocking resistance between individual soil contact grains.
* **$\beta$ (Slope Angle) [degrees]:** The geometric inclination steepness of the slope face relative to a true horizontal datum.
* **$H$ (Slope Height) [meters]:** The vertical elevation depth profile representing the heavy driving mass of the material.
* **$\gamma$ (Soil Unit Weight) [kN/m³]:** The bulk weight density that translates directly into gravity-driven downward force.

---

## 🧠 Architectural Overview & Technical Stack

In traditional geotechnical engineering consultancy, calculating slope stability involves executing iterative calculations (such as Bishop’s, Janbu’s, or Morgenstern-Price methods). While highly accurate, executing these repetitive calculus operations inside web processing loops can cause massive frontend latency, rendering dashboards sluggish.

This project implements a streamlined, two-tiered software pipeline:
1. **The Training Environment (Notebook Layer):** A deterministic Python script sweeps a uniform distribution of parameters to establish a balanced dataset. It splits the array into target ($y$) and features ($X$) before training a 50-tree **Random Forest Regressor** using `scikit-learn` to map complex, non-linear safety boundaries.
2. **The Production Environment (Deployment Layer):** The active model weights are serialized into a binary `.pkl` file via `joblib`. The live Streamlit app calls `joblib.load()` on startup, pulling the pre-trained asset directly into memory to instantly approximate structural safety without hardcoding math blocks.

### Full Technology Stack:
* **UI/Frontend Interface:** Streamlit (Dynamic widgets and mathematical LaTeX rendering)
* **Machine Learning Pipeline:** Scikit-Learn (Ensemble Regressors, Hyperparameter Mapping)
* **Model Caching & Serialization:** Joblib (High-efficiency binary array compression)
* **Data Structuring Engine:** Pandas & NumPy (Synthetic vector matrices)
* **Core Language Environment:** Python 3.10+

---

## 📊 Factor of Safety ($FoS$) Interpretation Scale

The model's real-time outputs are dynamically parsed across standardized civil engineering thresholds:

| FoS Range | Structural Stability Status | Professional Engineering Action Implication |
| :--- | :--- | :--- |
| **FoS < 1.0** | 🔴 Unstable (Active Failure) | Immediate remediation, soil nailing, or heavy retaining walls required. |
| **1.0 ≤ FoS < 1.3** | 🟡 Marginally Stable / Critical | High risk profile. Detailed site investigation and field monitoring mandatory. |
| **1.3 ≤ FoS < 1.5** | 🟢 Acceptable (Temporary Slopes) | Structurally compliant for short-term excavation or low-risk projects. |
| **FoS ≥ 1.5** | 🟢 Safe (Permanent Civil Design) | Meets standard long-term target safety parameters for civil works. |

---

