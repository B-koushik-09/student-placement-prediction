# import pickle

# model = pickle.load(open('model.pkl','rb'))

# '''
# Age :- Enter Age

# Gender :-   Male : 1 ,
#             Female : 0

# Stream :-   'Electronics And Communication' : 1,
#             'Computer Science' : 2,
#             'Information Technology' : 3,
#             'Mechanical' : 4,
#             'Electrical' : 5,
#             'Civil' : 6.

# Internships :- No. Of Internships Done.

# CGPA :- CGPA of Student

# Hostel :- Live In Hostel : 1,
#           Not Live in Hostel : 0.

# HistoryofBacklogs :- Yes : 1
#                      No : 0.

# model.predict([[Age,Gender,Stream,Internships,CGPA,Hostel,HistoryOfBacklogs]])

# '''
# data = [[21,1,2,0,9,0,0]]
# print("Placed" if model.predict(data) == 1 else "Not Placed")
# print(f"Your Chances Of Getting Placed {model.predict_proba(data)[0][1] * 100 :.2f} %")

# print('\n','*' * 50,'\n')

# data = [[25,1,4,1,7,1,0]]
# print("Placed" if model.predict(data) == 1 else "Not Placed")
# print(f"Your Chances Of Getting Placed {model.predict_proba(data)[0][1] * 100 :.2f} %")

# print('\n','*' * 50,'\n')

# data = [[25,1,2,0,8,1,0]]
# print("Placed" if model.predict(data) == 1 else "Not Placed")
# print(f"Your Chances Of Getting Placed {model.predict_proba(data)[0][1] * 100 :.2f} %")

# print('\n','*' * 50,'\n')

# data = [[0,0,0,0,0,0,0]]
# print("Placed" if model.predict(data) == 1 else "Not Placed")
# print(f"Your Chances Of Getting Placed {model.predict_proba(data)[0][1] * 100 :.2f} %")

# print('\n','*' * 50,'\n')

# age = int(input("Enter Your Age (min 19 - max 31) : "))
# if age > 31:
#     age = 31
# elif age < 19:
#     age = 19

# print('''Gender :-   Male : 1 ,
#             Female : 0''')

# gender = int(input("Enter Your Gender : "))
# if gender > 1:
#     gender = 1

# print('''Stream :-   'Electronics And Communication' : 1,
#             'Computer Science' : 2,
#             'Information Technology' : 3,
#             'Mechanical' : 4,
#             'Electrical' : 5,
#             'Civil' : 6.''')

# stream = int(input("Enter Your Stream : "))
# if stream == 0 or stream > 6:
#     stream = 6

# internship = int(input("Enter No. Of Internship Done (min 0 - max 3) : "))
# if internship > 3:
#     internship = 3

# cgpa = float(input("Enter Your CGPA : "))
# cgpa = int(cgpa)
# if cgpa > 10:
#     cgpa = 10

# print('''Hostel :- Live In Hostel : 1,
#           Not Live in Hostel : 0.''')

# hostel = int(input("Do You Live In Hostel : "))
# if hostel > 1:
#     hostel = 1

# print('''HistoryofBacklogs :- Yes : 1
#                      No : 0.''')
# hbl = int(input("Do You Have Any History Of Backlogs: "))
# if hbl > 1:
#     hbl = 1

# print('\n','*' * 50,'\n')

# data = [[age , gender , stream , internship , cgpa , hostel , hbl]]
# pred = model.predict(data)

# if pred:
#     print("You Have High Chances Of Getting Placed")
# else:
#     print("You Have Low Chances Of Getting Placed")

# print('\n','*' * 50,'\n')

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
