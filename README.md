# Greeting Card Slogan Generator

## Overview

This Python script is a Greeting Card Slogan Generator that fetches the top 5 news headlines and uses the ChatGPT API to create comical and witty slogans to put on greeting cards. Additionally, it generates prompts for stable diffusion to go with the slogans.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- `beautifulsoup4` library (`pip install beautifulsoup4`)
- `openai` library (`pip install openai`)

## Usage

1. Clone this repository or download the `main.py` file.

2. Set up your API keys:
   - Get a News API key from your preferred news service.
   - Get a ChatGPT API key from OpenAI (GPT-3.5-turbo model).

3. Replace  `'YOUR_CHATGPT_API_KEY'` in `main.py` with your actual API keys.

4. Run the Python script:

   ```bash
   python main.py
