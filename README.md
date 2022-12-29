Voice Assistant in Python - "Ella"

This project was created alongside a tutorial found here: https://www.udemy.com/course/total-python/

Key Learning Objectives and Renforcements:

Variables and Functions
Exceptions
Loops
Importing and using Modules


Welcome to the repository for a voice assistant created in Python! This project aims to demonstrate how to use Python to build a simple voice assistant that can respond to voice commands and perform basic tasks.

Prerequisites
To get started with this project, you'll need the following:

A computer with Python installed (this project was developed using Python 3.7, but should work with other versions as well)
A microphone and speakers (or a headset with a microphone)
Installation
To install the necessary dependencies for this project, run the following command:

Copy code
pip install -r requirements.txt
Usage
To start the voice assistant, run the following command:

Copy code
python main.py
Once the voice assistant is running, you can issue voice commands by speaking into your microphone. The voice assistant will recognize your voice and respond accordingly.

Available Commands
Here are some of the commands that the voice assistant can recognize:


"What time is it?" - the voice assistant will tell you the current time
"What day is today?" - the voice assistant will tell you the current day of the week
"Do a Wikipedia search for" - the voice assistant will open a Wikipedia search for the specified term
"Play (song title) " or "Open Youtube" - the voice assistant will open a YouTube window with the specified song or video
"Open browser" - the voice assistant will open your default browser to the Google search webpage
"Tell a joke" - the voice assistant will tell a short joke for your amusement
"Search the internet for" - the voice assistant will perform a Google search

Customization
You can customize the voice assistant by adding additional commands and functionality. To do this, you'll need to modify the commands.py file. This file contains a list of dictionaries, each representing a command that the voice assistant can recognize. Each dictionary should contain the following keys:

'command': a string representing the command that the voice assistant should recognize (e.g. "What is the time?")
'function': the function that should be called when the command is recognized
'description': a brief description of what the command does

To add a new command, simply create a new dictionary with the above keys and append it to the commands list. Then, define the function that should be called when the command is recognized. This function should take in a single argument, args, which is a list of strings containing any additional arguments passed with the command (e.g. if the command is "Open [website]", args will contain the name of the website).

Contributing
If you'd like to contribute to this project, please fork the repository and make your changes in a separate branch. Then, submit a pull request and I'll review your changes.

Thanks for checking out this project! I hope you find it useful.