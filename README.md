The pyespeakr module is designed to allow Python to send simple and fast commands to the eSpeak speech engine. This version of the module is currently a beta release and includes only the core and basic features.

Below are some examples of how to use it.

Basic usage: directly speaking text

To play a text directly, use the following command:
----------------------------
import pyespeakr

pyespeakr.run("en", "Hello", 175)
----------------------------
In the first argument, you select the language.
In the second argument, you write the text in that selected language.
The third argument, 175, defines the reading speed in words per minute.


---

Saving text to an audio file

To save text as an audio file, you can use:
----------------------------
import pyespeakr

pyespeakr.save_to_file("en", "Hello", 175, "file.mp3")
----------------------------
The first three arguments follow the same rules as the previous command.
The fourth argument specifies the output file name where the audio will be saved.


---

Reading and playing a text file

To read the content of a file and play it directly, use:
----------------------------
import pyespeakr

pyespeakr.open_file("en", "file.txt", 175)
----------------------------
In this command, the first argument selects the language.
The second argument is the file name (including its extension) whose content will be read.
The third argument defines the reading speed.
After execution, the text inside the file will be spoken aloud.


---

Converting a text file to audio

To read a file and save its content as an audio file:
----------------------------
import pyespeakr

pyespeakr.file_to_voice("en", "file.txt", 175, "file.mp3")
----------------------------
The first argument selects the language.
The second argument is the file to be read.
The third argument sets the reading speed.
The fourth argument defines the output audio file name, which will be created after execution containing the spoken content of the input file.


---

Installation requirements

To use this module correctly, the eSpeak engine must be installed on your system.

Then install the Python package using:

pip install pyespeakr

After installation, you can import and use it in your projects.

The module is available on PyPI:

https://pypi.org/project/pyespeakr/#description