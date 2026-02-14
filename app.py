import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def base():
    return render_template('form.html')


@app.route('/predict', methods=['GET'])
def predict():

    age = int(request.args.get('age'))
    gender = int(request.args.get('gender'))
    stream = int(request.args.get('stream'))
    internship = int(request.args.get('internship'))
    cgpa = float(request.args.get('cgpa'))   # float
    hostel = int(request.args.get('hostel'))
    backlogs = int(request.args.get('backlogs'))

    arr = np.array([[age, gender, stream, internship, cgpa, hostel, backlogs]])

    output = model.predict(arr)

    if output == 1:
        out = 'High'
    else:
        out = 'Low'

    return render_template('output.html', output=out)

if __name__ == '__main__':
    app.run(debug=True)
