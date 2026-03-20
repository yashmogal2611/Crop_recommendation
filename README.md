# 🌾 Regenerative Crop Rotation Recommender

An AI-powered web application that recommends the best crop to grow based on soil conditions and generates a 4-season regenerative crop rotation plan.

---

## 🎯 Problem Statement

Farmers who grow the same crop repeatedly on the same land deplete soil nutrients, leading to dependency on chemical fertilizers. This project solves that by recommending smart crop rotation plans based on real soil data — promoting sustainable and regenerative agriculture.

---

## 💡 Solution

A Machine Learning model trained on soil parameters that:
- Recommends the best crop for current soil conditions
- Generates a 4-season crop rotation plan
- Explains WHY a crop was recommended (AI explainability)
- Suggests biofertilizers instead of chemicals

---

## 🚀 Features

- 🧪 Input 7 soil & climate parameters (N, P, K, pH, temperature, humidity, rainfall)
- 🤖 Random Forest ML model with ~99% accuracy
- 🎯 Crop recommendation with confidence score
- 🔄 4-season regenerative rotation plan
- 📊 Feature contribution chart (AI explanation)
- 🌿 Biofertilizer recommendation
- 🌐 Interactive web app built with Streamlit

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Scikit-learn | Machine Learning (Random Forest) |
| Pandas & NumPy | Data processing |
| Matplotlib | Data visualization |
| Streamlit | Web app UI |
| Google Colab | Model training |

---

## 📦 Dataset

- **Name:** Crop Recommendation Dataset
- **Source:** Kaggle (atharvaingle/crop-recommendation-dataset)
- **Size:** 2,200 rows × 8 columns
- **Crops:** 22 different crops
- **Features:** N, P, K, temperature, humidity, pH, rainfall

---

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YourUsername/crop-rotation-recommender.git
cd crop-rotation-recommender
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

### 4. Open in browser
```
http://localhost:8501
```

---

## 📊 Model Performance

| Metric | Score |
|---|---|
| Accuracy | ~99% |
| Model | Random Forest (100 trees) |
| Train/Test Split | 80% / 20% |
| Cross Validation | Stratified |

---

## 🔄 Crop Rotation Logic

The rotation plan is based on regenerative agriculture principles:
- Legumes after cereals (to fix nitrogen naturally)
- Deep-rooted crops after shallow-rooted ones
- Biofertilizer recommendations instead of chemicals

Example rotation:
```
Season 1 → Rice
Season 2 → Lentil (fixes nitrogen)
Season 3 → Chickpea
Season 4 → Maize
```

---

## 🌿 Why Regenerative Agriculture?

- Reduces dependency on chemical fertilizers
- Improves soil health over time
- Increases long-term crop yield
- Environmentally sustainable farming

---

## 📁 Project Structure
```
crop-rotation-recommender/
├── app.py                    ← Streamlit web app
├── crop_model.pkl            ← Trained ML model
├── label_encoder.pkl         ← Label encoder
├── Crop_recommendation.csv   ← Dataset
├── requirements.txt          ← Dependencies
└── README.md                 ← Project documentation
```

---

## 👨‍💻 Author

**Your Name**
- LinkedIn: linkedin.com/in/yourname
- GitHub: github.com/yourname
- Email: youremail@gmail.com

---

## 🙏 Acknowledgements

- Dataset by Atharva Ingle on Kaggle
- Inspired by Jacob AI's regenerative agriculture platform
- Built as part of Agriculture AI project portfolio
```

---

Press **Ctrl + S** to save.

Now your folder looks like:
```
CROP_RECOMMENDATION/
├── app.py
├── crop_model.pkl
├── label_encoder.pkl
├── Crop_recommendation.csv
├── requirements.txt
└── README.md          ← new!
