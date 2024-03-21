from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import random

app = Flask(__name__)

# Dummy quiz data (replace with your own quiz questions)
quiz_data = pd.read_csv('qa.csv')

# create quiz questions for one time
quiz_questions = []
for _ in range(10):
    question = dict(quiz_data.iloc[random.randint(0, len(quiz_data) - 1)])
    question = {
        'question': question['question'],
        'options': [question['a'], question['b'], question['c'], question['d']],
        'answer': question['answer']
    }
    quiz_questions.append(question)

@app.route('/')
def index():
    return render_template('index.html', quiz_data=quiz_questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for question in quiz_questions:
        user_answer = request.form.get(question['question'])
        if user_answer == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=10)

if __name__ == '__main__':
    app.run(debug=True)