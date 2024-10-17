# AI Routing Agent

The **AI Routing Agent** is a command-line tool that utilizes various AI models to perform different text processing tasks. It can funify text, summarize text, multiply numbers, and count vowels in a given input.

## Features

- **Funify Text**: Makes input text funnier using the DialoGPT model.
- **Summarize Text**: Summarizes input text using a pretrained BART model.
- **Multiply Numbers**: Multiplies a list of numbers provided by the user.
- **Count Vowels**: Counts the number of vowels in the given text.

## Folder Structure

```
project_root/
├── ai_routing_agent.py
├── tools/
│   ├── __init__.py
│   ├── text_summarizer.py
│   ├── text_funifier.py
│   ├── multiplication_tool.py
│   └── vowel_counter.py
├── requirements.txt
└── README.md
```

## Installation

  Just run "pip install -r requirements.txt"


## Usage

Run the AI Routing Agent from the command line:

```Command Prompt
python ai_routing_agent.py 
```

### Supported Commands

- **Funify Text**:
  ```
  funify: <your-text>
  ```

- **Summarize Text**:
  ```
  summarize: <your-text>
  ```

- **Multiply Numbers**:
  ```
  multiply: <number1> <number2> ... <numberN>
  ```

- **Count Vowels**:
  ```
  count_vowels: <your-text>
  ```

## Requirements

- [Transformers](https://huggingface.co/transformers/)
- PyTorch

