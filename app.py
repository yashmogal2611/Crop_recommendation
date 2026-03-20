import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Crop Rotation Recommender",
    page_icon="🌾",
    layout="wide"
)

@st.cache_resource
def load_model():
    model = pickle.load(open('crop_model.pkl', 'rb'))
    le    = pickle.load(open('label_encoder.pkl', 'rb'))
    return model, le

model, le = load_model()

rotation_rules = {
    'rice':        ['lentil',    'chickpea',   'maize'],
    'maize':       ['soybean',   'wheat',      'groundnut'],
    'wheat':       ['chickpea',  'mustard',    'lentil'],
    'chickpea':    ['maize',     'wheat',      'rice'],
    'lentil':      ['rice',      'maize',      'wheat'],
    'cotton':      ['wheat',     'soybean',    'chickpea'],
    'sugarcane':   ['wheat',     'mustard',    'potato'],
    'mango':       ['groundnut', 'soybean',    'maize'],
    'banana':      ['rice',      'maize',      'chickpea'],
    'coffee':      ['maize',     'groundnut',  'lentil'],
    'jute':        ['rice',      'wheat',      'chickpea'],
    'coconut':     ['banana',    'groundnut',  'maize'],
    'papaya':      ['maize',     'lentil',     'chickpea'],
    'orange':      ['wheat',     'maize',      'groundnut'],
    'apple':       ['wheat',     'chickpea',   'mustard'],
    'grapes':      ['wheat',     'lentil',     'maize'],
    'watermelon':  ['maize',     'chickpea',   'wheat'],
    'muskmelon':   ['maize',     'lentil',     'wheat'],
    'kidneybeans': ['maize',     'wheat',      'rice'],
    'pigeonpeas':  ['maize',     'wheat',      'chickpea'],
    'mothbeans':   ['wheat',     'maize',      'lentil'],
    'mungbean':    ['rice',      'maize',      'wheat'],
    'blackgram':   ['rice',      'wheat',      'maize'],
    'pomegranate': ['wheat',     'groundnut',  'maize'],
}

def get_rotation_plan(crop):
    crop    = crop.lower()
    seasons = rotation_rules.get(crop, ['wheat', 'maize', 'chickpea'])
    return [crop] + seasons

st.title("🌾 Regenerative Crop Rotation Recommender")
st.markdown("##### Enter your soil details below to get a smart AI-powered crop plan")
st.markdown("---")

st.subheader("🧪 Soil & Climate Details")

col1, col2, col3 = st.columns(3)

with col1:
    N  = st.slider("Nitrogen (N)",   0,   140,  50)
    P  = st.slider("Phosphorus (P)", 0,   145,  50)
    K  = st.slider("Potassium (K)",  0,   205,  50)

with col2:
    temperature = st.slider("Temperature (°C)", 0.0,  50.0, 25.0)
    humidity    = st.slider("Humidity (%)",      0.0, 100.0, 60.0)

with col3:
    ph       = st.slider("Soil pH",         0.0,  14.0,  6.5)
    rainfall = st.slider("Rainfall (mm)",   0.0, 300.0, 100.0)

st.markdown("---")

if st.button("🚀 Get My Crop Rotation Plan", use_container_width=True):

    input_data = pd.DataFrame(
        [[N, P, K, temperature, humidity, ph, rainfall]],
        columns=['N','P','K','temperature','humidity','ph','rainfall']
    )

    pred_idx   = model.predict(input_data)[0]
    pred_crop  = le.inverse_transform([pred_idx])[0]
    pred_proba = model.predict_proba(input_data)[0]
    confidence = round(pred_proba[pred_idx] * 100, 2)

    st.markdown("---")
    st.subheader("🎯 Recommendation Result")

    res_col1, res_col2 = st.columns(2)

    with res_col1:
        st.success(f"Recommended Crop: **{pred_crop.upper()}**")
        st.metric("Model Confidence", f"{confidence}%")

    with res_col2:
        top3_idx   = np.argsort(pred_proba)[::-1][:3]
        top3_crops = le.inverse_transform(top3_idx)
        top3_probs = pred_proba[top3_idx] * 100
        st.markdown("**Top 3 crop options:**")
        for crop, prob in zip(top3_crops, top3_probs):
            st.progress(int(prob), text=f"{crop.title()} — {prob:.1f}%")

    st.markdown("---")
    st.subheader("🔄 4-Season Rotation Plan")

    plan    = get_rotation_plan(pred_crop)
    seasons = ["🌱 Season 1 (Current)", "🌿 Season 2", "🌾 Season 3", "🍀 Season 4"]
    colors  = ["#2ecc71", "#27ae60", "#1abc9c", "#16a085"]

    s1, s2, s3, s4 = st.columns(4)
    for col, season, crop, color in zip([s1,s2,s3,s4], seasons, plan, colors):
        col.markdown(
            f"""<div style='background-color:{color}22; border:1px solid {color};
            border-radius:10px; padding:16px; text-align:center;'>
            <p style='color:{color}; font-size:13px; margin:0'>{season}</p>
            <h3 style='margin:8px 0'>{crop.title()}</h3>
            </div>""",
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.subheader("📊 Why this crop? (AI Explanation)")

    feature_names  = ['N','P','K','temperature','humidity','ph','rainfall']
    feature_values = input_data.iloc[0].values
    importances    = model.feature_importances_
    normalized     = feature_values / np.array([140,145,205,50,100,14,300])
    contributions  = importances * normalized
    colors_bar     = ['#2ecc71' if c >= np.median(contributions)
                      else '#e74c3c' for c in contributions]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(feature_names, contributions, color=colors_bar, edgecolor='white')
    ax.axvline(x=np.median(contributions), color='black',
               linewidth=0.8, linestyle='--')
    ax.set_title(f'What drove the {pred_crop.upper()} recommendation?')
    ax.set_xlabel('Contribution Score')
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")
    st.subheader("🌿 Biofertilizer Recommendation")

    bio_tips = {
        'rice':      'Use Azolla and Blue-Green Algae to fix nitrogen naturally.',
        'maize':     'Apply Mycorrhizal fungi to improve phosphorus uptake.',
        'wheat':     'Use Rhizobium + Azotobacter for nitrogen fixation.',
        'chickpea':  'Rhizobium inoculant works best — fixes its own nitrogen!',
        'default':   'Use compost + Trichoderma to improve overall soil health.',
    }
    tip = bio_tips.get(pred_crop.lower(), bio_tips['default'])
    st.info(f"💡 {tip}")

    st.success("✅ Analysis complete! Save this plan for your farm.")