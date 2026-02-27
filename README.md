# College Student Placement Prediction WebApp

Welcome to the College Student Placement Prediction WebApp! This project leverages machine learning to predict the placement outcomes of college students. The web application is built using Flask for the backend and various other technologies for data processing and visualization.

## Introduction

This web application uses machine learning algorithms to predict whether a student will be placed or not based on their academic and extracurricular performance. It provides insights and visualizations to help understand the factors affecting placement.


## Features

- Predict placement status based on student data
- Visualize data distributions and relationships
- Interactive and user-friendly web interface


## Technologies Used:
* Programming Languages: Python, JavaScript
* Web Framework: Flask
* Data Processing and Analysis: NumPy, pandas, scikit-learn
* Data Visualization: Matplotlib, seaborn
* Frontend: HTML, CSS
* IDE and Tools: Anaconda Navigator, Jupyter Notebook, VS Code

## Machine Learning Model

- Algorithm: Decision Tree Classifier  
- Data preprocessing: Categorical encoding for Gender and Stream  
- Train-test split used for model training  
- Model saved using `pickle` and integrated into Flask app 

## Output

The user enters student details through the web form and the model predicts:
High → High chances of placement
Low → Low chances of placement

## How to Run the Project

1. Install required libraries:
   pip install flask pandas numpy scikit-learn matplotlib seaborn 

2. Train the model:
   python model.py

3. Run the Flask app:
   python app.py

4. Open in browser:
   http://127.0.0.1:5000



https://www.canva.com/design/DAGGMw0Q4KA/dGucRITOOa67dXWgtQc_rQ/edit



