# AI Assistant with Telegram Bot(dsssGPT)

## Project Overview

This project is based on a masters course excercise completion which demonstrates the implementation of an AI assistant powered by a Large Language Model (LLM), accessible through a Telegram bot. The system integrates a Telegram bot interface with a locally hosted LLM backend to process user messages and provide intelligent responses.

### Features:

1. **Telegram Bot Integration**: A custom Telegram bot created using BotFather.
2. **Message Handling**: The bot receives and processes user input, forwarding it to the backend for inference.
3. **LLM Backend**: The assistant uses a locally hosted LLM (e.g., TinyLlama) for natural language processing.
4. **Favorite Animal Interaction**: Users can ask the assistant for facts about their favorite animal.
5. **GPU Acceleration Support**: Configured for efficient LLM inference on compatible hardware.

---

## How It Works

1. **Bot Setup**: The Telegram bot `dsssGPT_bot` ([t.me/dsssGPT_bot](t.me/dsssGPT_bot)) is set up using BotFather, with a secure API token for communication.
2. **Message Flow**:
   - Users send messages to the bot.
   - The bot forwards the messages to the local server.
   - The server processes the input using the LLM and sends the response back to the user.
3. **Inference**: The LLM performs text-based inference locally, leveraging GPU acceleration (if available) for faster processing. ([TinyLlama](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0))
   
---
## Usage Instructions

1. Start the bot via [dsssGPT_bot](t.me/dsssGPT_bot).
2. Send a message (e.g., "/start") to interact with the assistant.
3. Ask anything to see the LLM-powered response.

---

## Acknowledgments

- **Telegram Bot API** for seamless integration.
- **TinyLlama** (LLM) for backend intelligence.
- FAU- Data Science Survival Skills [DSSS] Course Organizers.
