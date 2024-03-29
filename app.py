from flask import Flask, render_template, request, jsonify
import requests
import os
import openai

app = Flask(__name__)


# Paste your API KEY HERE
openai.api_key = "YOUR API KEY HERE"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get user input from the form
    story_details = request.json['story-details']
    genre = request.json['genre']
    character_name = request.json['character1-name']
    character_sex = request.json['character1-sex']
    reader_age = request.json['reader-age'] 

    # Generate three stories using OpenAI
    stories = []
    # Generate three versions of the story
    story = f"You are an expert storywriter. Use this framework 1.A captivating hook 2.Describe scenario.3. Describe character.4. write story using these details. Remember you are writing the final draft {story_details}\n\nGenre: {genre}\n\nCharacter: {character_name}, {character_sex}. write for a {reader_age} year old reader.Output the full story in paragraph format"

    generated_stories = []

    # Call OpenAI API to generate the story based on the prompt
    response1 = openai.Completion.create(model="text-davinci-003", prompt=story, temperature=0.1, max_tokens=4000, top_p=0.1)
    response2 = openai.Completion.create(model="text-davinci-003", prompt=story, temperature=0.5, max_tokens=4000, top_p=0.5)
    response3 = openai.Completion.create(model="text-davinci-003", prompt=story, temperature=0.9, max_tokens=4000, top_p=0.9)

    generated_story1 = response1['choices'][0].text.strip()
    generated_story2 = response2['choices'][0].text.strip()
    generated_story3 = response3['choices'][0].text.strip()

    stories.extend([generated_story1, generated_story2, generated_story3])

    # Return the generated stories as a JSON response
    return jsonify({'stories': stories})

if __name__ == '__main__':
    app.run(debug=True)