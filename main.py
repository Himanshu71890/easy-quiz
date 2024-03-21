from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy quiz data (replace with your own quiz questions)
quiz_data = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Madrid'],
        'answer': 'Paris'
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['Jupiter', 'Mars', 'Earth', 'Venus'],
        'answer': 'Jupiter'
    },
    {
        'question': 'Who wrote "Romeo and Juliet"?',
        'options': ['William Shakespeare', 'Charles Dickens', 'Jane Austen', 'Mark Twain'],
        'answer': 'William Shakespeare'
    }
]

@app.route('/')
def index():
    return render_template('index.html', quiz_data=quiz_data)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for question in quiz_data:
        user_answer = request.form.get(question['question'])
        if user_answer == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(quiz_data))

if __name__ == '__main__':
    app.run(debug=True)