## Streamlit Chatbots

Three small Streamlit apps that run local chat personas through Ollama. Each app uses a different combination of Ollama's API (chat vs generate) and persona style.

### **app.py**

A minimal chatbot using the Atlas travel-guide persona and Ollama's chat() API with full conversation history.

- **Persona**: Atlas, a global travel guide and trip planner.
- **API used**: ollama.chat() — sends the entire message history  on every turn, so the model has context from earlier in the conversation.
- **Roles**: uses valid Ollama roles (system, user, assistant); the system prompt is hidden from the rendered chat history.

### **simple_with_stream.py**

- **Persona**: same Atlas travel-guide persona as app.py.
- **API used**: ollama.chat(..., stream=True) — iterates over response chunks and updates the displayed message incrementally, rather than waiting for the full reply.
- **Roles**: same valid-role setup as app.py.

### **simple_generate_chat.py**

A single-turn tool built around a Sage summarization persona, using generate() rather than chat().

- **Persona**: Sage, a summarizer that condenses long or messy text into clear, faithful summaries without adding information.
- **API used**: ollama.generate() — a one-shot completion call. The persona and the user's text are combined into a single prompt string for each request, rather than maintained as a running message history.
- **Use case**: pasting in an article, notes, or any block of text and getting a structured summary back.