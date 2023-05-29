# Story Completion Application


A creative and interactive story completion application powered by OpenAI API. This application allows users to input a story prompt or sentence and generates three unique variations of the story using the power of natural language processing and machine learning.

## Features

- **Easy-to-Use Interface**: Simple and intuitive user interface makes it effortless to interact with the application.
- **Story Generation**: Generate three distinct versions of a given story prompt, adding a touch of creativity and novelty to your writing.
- **Powered by OpenAI**: Leverages the OpenAI API to produce high-quality and coherent story completions.
- **Local Deployment**: Run the Flask backend locally by executing the `app.py` file.

## How to Use

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/story-completion-app.git

Make sure you have Python 3.x installed on your system.

Navigate to the project directory:
 
 ```shell
cd story-completion-app

```
Install the required dependencies:

```shell
pip install -r requirements.txt
```
Open the app.py file and insert your OpenAI API key in the designated field:


# Replace 'YOUR_API_KEY' with your actual OpenAI API key
```
openai.api_key  = 'YOUR_API_KEY'

```
Save the changes and run the Flask backend by executing the following command:
```
python app.py
```
Open your web browser and visit http://localhost:5000 to access the Story Completion Application.

Enter a story prompt or sentence into the input field and click the "Generate" button. The application will generate three different versions of the story for you to explore and inspire your creative writing.

