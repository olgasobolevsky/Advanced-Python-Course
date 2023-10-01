from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie_app.temperature import Temperature
from calorie_app.calculators import CalorieCalculator

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CaloriesCalculatorFormPage(MethodView):
    def get(self):
        calories_calculator_form = CaloriesCalculatorForm()
        return render_template('calories_form_page.html',
                               caloriesform=calories_calculator_form)

    def post(self):
        calories_calculator_form = CaloriesCalculatorForm(request.form)
        """ Get temperature """
        temperature = Temperature(country=calories_calculator_form.country.data,
                                  city=calories_calculator_form.city.data).get()
        """ Calculate calories"""
        calories = CalorieCalculator(weight=float(calories_calculator_form.weight.data),
                                     height=float(calories_calculator_form.height.data),
                                     age=float(calories_calculator_form.age.data),
                                     temperature=temperature).calculate()

        return render_template('calories_form_page.html',
                               result=True,
                               caloriesform=calories_calculator_form,
                               calories=calories)


class CaloriesCalculatorForm(Form):
    weight = StringField("What is your weight: ")
    height = StringField("What is your height: ")
    age = StringField("What is your age: ")
    country = StringField("What is your country: ")
    city = StringField("What is your city: ")

    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_func=CaloriesCalculatorFormPage.as_view('calories_form_page'))

app.run(debug=True)
