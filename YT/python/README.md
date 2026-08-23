# Python for AI — Complete Course Notes & Study Guide

Welcome to the comprehensive revision notes and documentation for the **Python for AI - Full Beginner Course** by Dave Ebbelaar (Data Lumina). This guide covers everything from professional development environment setup to building production-ready AI applications.

---

## Table of Contents

1. [Course Philosophy & Strategy](https://www.google.com/search?q=%231-course-philosophy--strategy)
2. [Development Environment Setup](https://www.google.com/search?q=%232-development-environment-setup)
3. [Virtual Environments & Package Management](https://www.google.com/search?q=%233-virtual-environments--package-management)
4. [Python Core Fundamentals](https://www.google.com/search?q=%234-python-core-fundamentals)
5. [Data Handling & File Operations](https://www.google.com/search?q=%235-data-handling--file-operations)
6. [Working with External APIs & Libraries](https://www.google.com/search?q=%236-working-with-external-apis--libraries)
7. [Capstone: Building an AI Chat Assistant](https://www.google.com/search?q=%237-capstone-building-an-ai-chat-assistant)
8. [Best Practices & Quick Reference](https://www.google.com/search?q=%238-best-practices--quick-reference)

---

## 1. Course Philosophy & Strategy

* **AI-First Python Learning:** Traditional Python courses spend excessive time on abstract concepts. This course focuses strictly on what is required to build AI systems, manipulate data, and integrate Large Language Models (LLMs).
* **Setup-First Approach:** Most beginners struggle with environment configurations rather than writing syntax. Establishing a production-grade workspace prevents downstream dependency conflicts.
* **Practical & Battle-Tested:** Every pattern taught reflects modern software standards used in real-world AI engineering.

---

## 2. Development Environment Setup

### 2.1 Installing Python

* **Windows Setup:**
1. Download the installer from `python.org/downloads`.
2. **CRITICAL STEP:** Check the box **"Add Python to PATH"** before clicking Install.
3. Verify installation in Command Prompt: `python --version`


* **macOS Setup:**
1. Check pre-installed version in Terminal (`Command + Space` $\rightarrow$ `terminal`): `python3 --version`
2. Install/update via official installer or Homebrew: `brew install python`



### 2.2 Code Editor (VS Code) Setup

* **Recommended Directory Naming:** Use kebab-case for project folders (e.g., `python-for-ai`).
* **Essential Extensions:**
* **Python** (Microsoft): Provides syntax highlighting, debugging, and code execution.
* **Pylance**: Language server providing high-performance auto-completion and static type checking.
* **Jupyter**: Enables interactive `.ipynb` notebook execution within VS Code.



### 2.3 VS Code Workspaces

Always convert project directories into a official VS Code workspace (`File` $\rightarrow$ `Save Workspace As...`). This preserves project-specific configurations, environment paths, and editor preferences across sessions.

---

## 3. Virtual Environments & Package Management

### 3.1 Understanding Virtual Environments

A virtual environment (`venv`) creates an isolated directory tree that contains a specific Python executable and its own set of installed packages. This prevents global version conflicts across projects.

### 3.2 Commands Cheat Sheet

| Task | Mac / Linux Terminal | Windows PowerShell / CMD |
| --- | --- | --- |
| **Create Environment** | `python3 -m venv .venv` | `python -m venv .venv` |
| **Activate Environment** | `source .venv/bin/activate` | `.venv\Scripts\activate` |
| **Deactivate** | `deactivate` | `deactivate` |
| **Select Interpreter (VS Code)** | `Cmd + Shift + P` $\rightarrow$ `Python: Select Interpreter` | `Ctrl + Shift + P` $\rightarrow$ `Python: Select Interpreter` |

### 3.3 Package Management with `pip`

* **Installing Libraries:**
```bash
pip install package_name

```


* **Managing Dependencies:**
```bash
# Freeze active dependencies to file
pip freeze > requirements.txt

# Install from existing requirements file
pip install -r requirements.txt

```



---

## 4. Python Core Fundamentals

### 4.1 Variables & Data Types

Python is dynamically typed. Common primitives and data structures include:

```python
# Primitive Types
user_name = "Dave"          # String (str)
agent_count = 5             # Integer (int)
temperature = 0.7           # Float (float)
is_active = True            # Boolean (bool)

# Data Structures
model_names = ["gpt-4o", "claude-3-5-sonnet", "llama-3"]  # List (ordered, mutable)
config = {"model": "gpt-4o", "max_tokens": 1000}          # Dictionary (key-value mapping)
unique_tags = {"ai", "python", "ai"}                      # Set (unique elements)

```

### 4.2 Control Flow

Direct execution paths using conditional checks and loops:

```python
# Conditionals
threshold = 0.8
if threshold > 0.9:
    print("High confidence")
elif threshold >= 0.5:
    print("Medium confidence")
else:
    print("Low confidence")

# Iteration
models = ["gpt-4o", "claude-3-5-sonnet"]
for model in models:
    print(f"Loading {model}...")

```

### 4.3 Functions & Modular Code

Functions group reusable blocks of code. Define explicit arguments and clear return statements:

```python
def format_prompt(system_prompt: str, user_query: str) -> str:
    """Combines system and user prompts into a structured payload."""
    return f"System: {system_prompt}\nUser: {user_query}"

prompt = format_prompt("You are a helpful assistant.", "Explain Python in 1 sentence.")

```

---

## 5. Data Handling & File Operations

### 5.1 Reading and Writing Files

Always use the `with` context manager when interacting with file I/O to ensure automatic stream closing:

```python
# Writing to a text file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("AI Agent Response Log")

# Reading from a text file
with open("output.txt", "r", encoding="utf-8") as f:
    content = f.read()

```

### 5.2 JSON Parsing (Standard for AI APIs)

Structured API communication relies heavily on JSON:

```python
import json

data = {"agent": "ChatBot", "status": "active", "memory_limit": 4096}

# Serialize to JSON String
json_string = json.dumps(data, indent=2)

# Deserialize back to Python Dictionary
parsed_data = json.loads(json_string)

```

---

## 6. Working with External APIs & Libraries

### 6.1 Making HTTP Requests (`requests`)

Interact with REST APIs using the standard `requests` module:

```python
import requests

response = requests.get("https://api.github.com")

if response.status_code == 200:
    payload = response.json()
    print("Connection Successful!")
else:
    print(f"Error: {response.status_code}")

```

### 6.2 Managing API Keys Safely

Never hardcode secrets inside source code. Use environment variables with `.env` files and `python-dotenv`:

1. Install module: `pip install python-dotenv`
2. Create `.env` file: `OPENAI_API_KEY="your_api_key_here"`
3. Load in Python:
```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env
api_key = os.getenv("OPENAI_API_KEY")

```



---

## 7. Capstone: Building an AI Chat Assistant

The final exercise of the course combines functions, loop controls, external API connectivity, and prompt structures into a local terminal chat interface.

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Environment Setup
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. Initialize Conversation Context
messages = [
    {"role": "system", "content": "You are a concise, helpful AI coding assistant."}
]

print("--- AI Chat Assistant Initialized (Type 'exit' to quit) ---")

# 3. Conversational Loop
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Ending session.")
        break

    # Append user context
    messages.append({"role": "user", "content": user_input})

    # Query API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    assistant_reply = response.choices[0].message.content
    print(f"\nAI: {assistant_reply}")

    # Append assistant context for memory
    messages.append({"role": "assistant", "content": assistant_reply})

```

---

## 8. Best Practices & Quick Reference

* **Environment Isolation:** Never install third-party packages directly into the global Python installation. Always activate a `.venv`.
* **Security:** Add `.env` and `.venv/` to your `.gitignore` file immediately upon initializing a git repository.
* **Code Readability:** Follow PEP 8 guidelines (use snake_case for functions/variables, PascalCase for classes).
* **Error Prevention:** Always inspect API return statuses and handle runtime failures gracefully using `try / except` blocks.