from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import speech_recognition as sr
import os


# Define a function to get voice input from the user
def get_voice_input():
    print("Press Enter and then speak your question:")
    input()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        question = r.recognize_google(audio)
        print(f"You said: {question}")
        return question
    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None


# Define a prompt template with a variable for the question and a placeholder for the answer
template = """Question: {question}

Answer: Let's think step by step."""

# Create a prompt object with the template and the input variable
prompt = PromptTemplate(template=template, input_variables=["question"])

# Create a callback manager to stream the output token by token
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Create a LLaMA object with the model path and the callback manager
# Make sure the model path is correct for your system!
llm = LlamaCpp(
    model_path="/Users/oluwaseunolaoya/Documents/LLM_Models/ggml-model-q4_0.bin", 
    callback_manager=callback_manager, 
    verbose=True,

    )

# Create a LLMChain object with the prompt and the LLaMA object
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Use a loop to get questions from the user and generate answers from LLaMA
while True:
    # Get a question from the user using voice input or keyboard input
    question = get_voice_input() or input("Please type a question: ")
    
    # Break the loop if the user wants to quit
    if question.lower() in ["quit", "exit", "stop"]:
        break
    
    # Run the LLMChain object with the question and print the final output
    output = llm_chain.run(question)

    # Sanitize the output string
    sanitized_output = output.replace("'", '"').replace("\n", " ").strip()
    print(output)



    # Use the sanitized output for text-to-speech
    os.system("say '" + sanitized_output + "'")










    