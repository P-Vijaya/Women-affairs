from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    if request.method =='POST':
        try:
            women_occupation = float(request.form['women_occupation'])
            husband_occupation = float(request.form['husband_occupation'])
            rate_marriage = float(request.form['rate_marriage'])
            age = float(request.form['age'])
            yrs_married = float(request.form['yrs_married'])
            children = float(request.form['children'])
            religious = float(request.form['religious'])
            educ = float(request.form['educ'])
            filename = 'logistic_regression.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))
            prediction = loaded_model.predict([[women_occupation,husband_occupation,
                                                rate_marriage,age,yrs_married,children,religious,educ]])
            print("Prediction values is:", prediction)
            return render_template('results.html', prediction=int(prediction))
        except Exception as e:
            print("The exception is:",e)
            return "Something is wrong"

    else:
        return render_template("index1.html")


if __name__ == '__main__':
    app.run(port=2000,debug=True)