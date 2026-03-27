# 🎓 Campus Placement Predictor - ML Web App

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

## 🌟 Project Overview
The **Campus Placement Predictor** is a data-driven web application designed to help students predict their likelihood of securing a job placement. By analyzing historical data and academic performance metrics, the app uses a **Decision Tree Classifier** to provide students with a "High" or "Low" placement probability, empowering them to focus on areas that need improvement.

---

## 🚀 Key Features
- **Placement Prediction**: Predicts your placement chances based on 7 key metrics.
- **Interactive Web Interface**: A clean, responsive UI built with Flask, HTML, and CSS.
- **Comprehensive Data Analysis**: A master Jupyter notebook covering the entire ML pipeline from EDA to Model Saving.
- **Real-time Results**: Instant feedback based on user-provided data.

---

## 🛠️ Technology Stack
### **Frontend**
- **HTML5 & CSS3**: Core structure and responsive design.
- **Jinja2**: Templating engine for Flask.

### **Backend**
- **Flask**: Lightweight web framework for Python.
- **Python 3.x**: Core programming language.

### **Machine Learning & Data Science**
- **Scikit-learn**: For building the Decision Tree classification model.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Matplotlib & Seaborn**: For data visualization during EDA.
- **Pickle**: For model serialization and deployment.

---

## 📊 The Machine Learning Model
The heart of this application is a **Decision Tree Classifier** trained on a dataset of college placement history.

### **Input Features**
1.  **Age**: Candidate's current age.
2.  **Gender**: Male (1) or Female (0).
3.  **Stream**: Academic discipline (Computer Science, IT, Electronics, etc.).
4.  **Internships**: Number of internships completed.
5.  **CGPA**: Cumulative Grade Point Average.
6.  **Hostel**: Whether the student lives in a hostel (1) or not (0).
7.  **Backlogs**: Number of history of backlogs (1) or not (0).

### **Output**
- **High**: Strong probability of placement.
- **Low**: Need for further skill enhancement.

---

## 📁 Project Structure
```text
Campus-Placement-Predictor/
├── static/                # CSS and static assets
├── templates/             # HTML templates (index, form, output)
├── Campus Placement Prediction Using ML.ipynb # Master Notebook (EDA + Training)
├── Papers/                # Research papers and reference documents
├── app.py                 # Main Flask application
├── model.pkl              # Serialized ML model
├── model.py               # Model training script
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignore configuration
└── README.md              # Project documentation
```

---

## 💻 Installation & Setup
Follow these steps to get the project running locally:

### **1. Clone the Repository**
```bash
git clone https://github.com/B-koushik-09/student-placement-prediction.git
cd student-placement-prediction
```

### **2. Set Up Virtual Environment (Recommended)**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. (Optional) Re-train the Model**
If you want to train the model from scratch using the dataset:
```bash
python model.py
```

### **5. Run the Application**
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser to see the app in action!

---


## 🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact 
Project Link: [https://github.com/B-koushik-09/student-placement-prediction](https://github.com/B-koushik-09/student-placement-prediction)
