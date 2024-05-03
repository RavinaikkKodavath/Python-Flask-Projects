import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Request error from Google Speech Recognition service: {e}")
        return ""

def main():
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "your name" in command:
            speak("I am a voice assistant created by OpenAI.")
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    main()
