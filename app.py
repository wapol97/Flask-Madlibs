from flask import Flask, render_template, request
from stories import stories

app = Flask(__name__)

@app.route('/')
def ask_questions():
    prompts = story.prompts
    return render_template('questions.html', prompts=prompts)

@app.route('/story')
def story_result():
    text = story.generate(request.args)
    return render_template('story.html', text=text)

@app.route('/questions')
def ask_questions():
    story_id = request.args["story_id"]
    story = stories[story_id]
    return render_template('story.html', title=story.title, text=text)