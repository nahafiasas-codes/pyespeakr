pyespeakr
pyespeakr is a Python module designed to send commands to the eSpeak text-to-speech engine.
The main goal of this module is to allow developers to control and use the eSpeak speech synthesis engine easily from Python.
This is currently a beta version, and more features will be added in future releases.
Usage
1. Speaking text directly
Python

import pyespeakr

pyespeakr.run("en", "Hello world", 175)

This command sends the text "Hello world" to the eSpeak engine and instructs it to:
Speak in English ("en")
Use a speed of 175 words per minute
You can use different languages and texts depending on what eSpeak supports. This module acts as a bridge to send those commands to the engine.
2. Speaking text from a file
Python

import pyespeakr

pyespeakr.open_file("en", "file.txt", 175)

This command reads the content of file.txt and sends it to the eSpeak engine to be spoken in English with a speed of 175 words per minute.
3. Checking the current version
Python

import pyespeakr

print(pyespeakr.__VERSION__)

This will print the current version of the module.
Summary
pyespeakr provides a simple interface to control the eSpeak TTS engine using Python, allowing text and file-based speech synthesis with customizable language and speed.

To download and use this package, follow the steps below:
Bash

pip install pyespeakr

Then import it into your project and use it. To run it, the minimum required Python version is 3.8 or higher.
Or you can visit the PyPI website using the link below and download the project:

https://pypi.org/project/pyespeakr/
