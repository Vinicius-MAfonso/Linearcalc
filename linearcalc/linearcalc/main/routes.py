from flask import Blueprint, render_template, request, redirect, url_for
from flask.globals import request
from .utils import Exercise

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')
@main.route('/about')
def about():
    return render_template('about.html')
@main.route('/calculator', methods=['GET','POST'])
def calculator():
    if request.method == 'POST':
        equations = request.form.getlist('equation')
        first_step = request.form.get('first_step')
        approximation = request.form.get('approximation')
        iterations = request.form.get('iterations')
        result = Exercise(equations)
        result.solve(float(first_step), int(approximation), int(iterations))
        return render_template('result.html', result=result)
    else:
        return render_template('calculator.html')
