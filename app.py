from flask import Flask, render_template, request, jsonify
import requests
import os
import openai

app = Flask(__name__)


# Load your API key from an environment variable or secret management service
openai.api_key = "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"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    story = data.get('prompt', '')
    
     # Call OpenAI API to generate the story based on the prompt
    response = openai.Completion.create(model="text-davinci-003", prompt=story, temperature=0.6)

    generated_story = response['choices'][0]['text']

    # Return the generated story to the user
    return jsonify({'story': generated_story})


if __name__ == '__main__':
    app.run(debug=True)
