

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv('archive/collegePlace.csv')

# Convert categorical columns to numbers
data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})

data['Stream'] = data['Stream'].map({
    'Electronics And Communication': 1,
    'Computer Science': 2,
    'Information Technology': 3,
    'Mechanical': 4,
    'Electrical': 5,
    'Civil': 6
})

# Features and target
X = data.drop('PlacedOrNot', axis=1)
y = data['PlacedOrNot']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

print("Model trained and saved successfully!")
