# Jarvis

Basic Jarvis is a voice-based assistant that uses natural language processing and machine learning to answer questions. It uses the LLaMA framework to generate answers on the fly using a prompt template and a pre-trained model. It also uses the speech_recognition library to get voice input from the user and convert it to text.

## Getting Started

To get started with Jarvis, you'll need to have Python 3.6 or higher installed on your system. You'll also need to install the following libraries:

* langchain
* speech_recognition

You can install them using pip:

pip install langchain
pip install speech_recognition

You'll also need to download the LLaMA model file or anyalternative from huggingface or anywhere

## Usage

To use Jarvis, simply run the following command in your terminal:

python jarvis.py

The script will prompt you to press Enter and then speak your question. It will then listen to your voice input and try to recognize it using Google Speech Recognition service. If successful, it will print your question and then generate an answer using the LLaMA model. The answer will be streamed token by token as it is generated.

You can ask any question that is related to general knowledge, such as:

* Who is the president of France?
* What is the capital of Australia?
* How many planets are there in the solar system?

The script will try to answer as best as it can, but keep in mind that it is still a work in progress and may not always produce accurate or complete answers.

In addition to printing the answer to the console, Jarvis will also read the answer out loud using the `os.system("say ...")` command. If you prefer not to use this feature, you can comment out or remove the relevant line in the `jarvis.py` file.

To exit the script, press `Ctrl+C`.

## Customization

You can customize Jarvis by modifying the `template` string in the `jarvis.py` file. The `template` string is a prompt template with a variable for the question and a placeholder for the answer. You can change the text to suit your needs, but make sure to keep the `{question}` and `Answer: Let's think step by step.` variables in the string.

You can also modify the path to the LLaMA model file and the callback manager settings in the `jarvis.py` file.

## Contributing

If you'd like to contribute to Jarvis, feel free to open an issue or submit a pull request. We welcome any feedback or suggestions you might have!

## Future Work

This is just a very basic model but i plan to do this in the future:

* Integrate with YOLOv8, a state-of-the-art object detection model, to enable Jarvis to answer questions based on visual input
* Improve the interactibility and conversation flow to make Jarvis feel more like a human assistant
* Add a cool user interface to enhance the user experience




