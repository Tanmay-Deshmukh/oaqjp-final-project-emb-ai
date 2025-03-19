'''Controls the backend server for the website.'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    '''Retrieve the text from the user and use the emotion detector on it. 
    After, respond with the confidence scores for each emotion.'''

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"""
    For the given statement, the system response is
    'anger': {response['anger']},
    'disgust': {response['disgust']},
    'fear': {response['fear']},
    'joy': {response['joy']},
    and 'sadness': {response['sadness']}.
    The dominant emotion is {response['dominant_emotion']}.
    """

@app.route('/')
def index():
    '''Render the index page.'''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
