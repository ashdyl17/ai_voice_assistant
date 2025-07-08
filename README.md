# 🗣️ Voice Assistant with Speech Recognition and AI Response

An intelligent, voice-activated assistant built with Python! Speak to your assistant, hear its response, and enjoy a seamless conversational experience powered by AI.

---

## 🚀 Features

* 🎧 **Speech Recognition**
  Capture voice input using the `speech_recognition` library and transcribe it using Google Speech Recognition API.

* 🗣️ **Text-to-Speech (TTS)**
  Respond audibly using `pyttsx3` for offline speech synthesis.

* 🤖 **Conversational AI**
  Generate intelligent, context-aware replies using [LangChain](https://www.langchain.com/) + `OllamaLLM` with the `mistral` model.

* 🧠 **Chat History**
  Keeps conversation history with `ChatMessageHistory` to maintain coherent dialogue.

* 🔀 **Dynamic Interaction Loop**
  Keeps listening and responding until you say "exit" or "stop".

---

## 🛠️ Requirements

* Python 3.8+
* Libraries:

  * `speechrecognition` – Speech-to-text
  * `pyttsx3` – Text-to-speech
  * `langchain-community` – For chat history
  * `langchain-ollama` – Interface with Ollama LLM
  * `pyaudio` – Required for mic input

---

## 📦 Installation

1. Clone this repo or download the script:

   ```bash
   git clone https://github.com/ashdyl17/ai_voice_assistant
   cd ai_voice_assistant
   ```

2. Install dependencies:

   ```bash
   pip install speechrecognition pyttsx3 langchain-community langchain-ollama pyaudio
   ```

3. **Set up Ollama:**

   * Install [Ollama](https://ollama.com/) and download the `mistral` model.
   * Make sure the Ollama service is running.

4. **Microphone Setup:**

   * Ensure your mic is connected and working.
   * On Linux/macOS, install `portaudio` if needed:

     ```bash
     sudo apt-get install portaudio19-dev  # For Ubuntu/Debian
     brew install portaudio                # For macOS with Homebrew
     ```

---

## ▶️ Usage

Run the assistant with:

```bash
python voice_assistant.py
```

### The assistant will:

* Greet you: *"Hello: I am your AI Assistant. How can I help you today?"*
* Listen for your voice input.
* Transcribe and process it.
* Respond with text and speech.

Say **"exit"** or **"stop"** to quit.

---

## 📄 Code Overview

### 🎧 Speech Recognition

* Uses `speech_recognition.Recognizer()` with Google API.
* Handles unrecognized speech and connection issues.

### 🗣️ Text-to-Speech

* Uses `pyttsx3` set to 180 WPM.
* The `speak(text)` function gives audible responses.

### 🤖 AI with LangChain + Ollama

* Uses `OllamaLLM(model="mistral")`
* Manages history with `ChatMessageHistory`
* Context is built via prompt templates

### ⟳ Looping Logic

* Continuously listens and processes until an exit command is spoken.

---

## ❓ Troubleshooting

* **Mic not working?** Check your device and input settings.
* **Ollama not responding?** Ensure it's running and model is loaded.
* **`pyaudio` install error?** Try installing `portaudio` first.
* **Speech issues?** Test your internet or consider using offline STT engines.

---
