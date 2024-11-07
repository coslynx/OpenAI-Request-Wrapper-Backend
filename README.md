<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
OpenAI-Request-Wrapper-Backend
</h1>
<h4 align="center">A Python backend for simplifying OpenAI API interactions</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="Framework-FastAPI-blue">
  <img src="https://img.shields.io/badge/Language-Python-red" alt="Language-Python-red">
  <img src="https://img.shields.io/badge/Database-SQLite-blue" alt="Database-SQLite-blue">
  <img src="https://img.shields.io/badge/LLMs-OpenAI-black" alt="LLMs-OpenAI-black">
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/OpenAI-Request-Wrapper-Backend?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/OpenAI-Request-Wrapper-Backend?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/OpenAI-Request-Wrapper-Backend?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview
This repository contains a Python backend server designed to streamline interactions with OpenAI's powerful AI models. The "AI Wrapper OpenAI Request Responder" provides a user-friendly interface for developers and individuals to leverage OpenAI's technology for various applications. This MVP focuses on simplifying the process of sending requests to OpenAI and receiving responses, eliminating the need for complex manual API call management.

## 📦 Features
|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The backend utilizes a lightweight framework like Flask or FastAPI for efficient routing and API management. |
| 📄 | **Documentation**  | The repository includes a comprehensive README file detailing the MVP's features, usage, and deployment instructions. |
| 🔗 | **Dependencies**   | The project relies on essential packages such as FastAPI, Uvicorn, Pydantic, OpenAI, and Requests for its functionality. |
| 🧩 | **Modularity**     | The code is structured for modularity, with separate files for handling requests, API interaction, and response processing. |
| 🧪 | **Testing**        | Unit tests are implemented to ensure the code's functionality and stability. |
| ⚡️  | **Performance**    | The backend optimizes communication with OpenAI APIs for swift responses, employing efficient request handling and response processing. |
| 🔐 | **Security**       | Robust security measures protect API keys and user data, ensuring secure handling of sensitive information. |
| 🔀 | **Version Control**| Utilizes Git for version control, employing a branching model for efficient development and maintenance. |
| 🔌 | **Integrations**   | Seamless integration with various applications and platforms is achieved using a REST API. |
| 📶 | **Scalability**    | The backend is designed to handle increasing request volumes efficiently.  |

## 📂 Structure
```text
[object Object]
```

## 💻 Installation
### 🔧 Prerequisites
- Python 3.10+
- `pip` package manager
- OpenAI API Key 

### 🚀 Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/coslynx/OpenAI-Request-Wrapper-Backend.git
   cd OpenAI-Request-Wrapper-Backend
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   - Open `.env` and replace `YOUR_OPENAI_API_KEY_HERE` with your actual OpenAI API key.
   - You can optionally set `DATABASE_URL` if you want to use a different database.

## 🏗️ Usage
### 🏃‍♂️ Running the Backend
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000
   ```
### ⚙️ Configuration
- The `utils/config.py` file handles environment variables like `OPENAI_API_KEY` and `DATABASE_URL`. You can change them in the `.env` file.
- The backend server listens on port 8000 by default. You can change this in `startup.sh` or by passing a different port to `uvicorn` when running the server.

### 📚 Examples
**Making a Text Generation Request**
```bash
curl -X POST http://localhost:8000/generate_text \
    -H "Content-Type: application/json" \
    -d '{"model": "text-davinci-003", "prompt": "Write a short story about a cat", "temperature": 0.7}'
```
**Response:**
```json
{
  "response": "Once upon a time, in a cozy little cottage nestled amidst rolling hills, there lived a mischievous tabby cat named Whiskers. Whiskers was known for his playful antics and his insatiable appetite for tuna."
}
```

## 🌐 Hosting
### 🚀 Deployment Instructions
1. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
4. **Run the application:**
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000
   ```
5. **Use a deployment platform like Heroku or AWS:**
   - Follow the specific instructions for your chosen platform.
   - Make sure to set up the environment variables (API keys, database credentials, etc.) as required by your chosen platform.

### 🔑 Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key.
- `DATABASE_URL`: Your database connection string (if using a database).

## 📜 API Documentation
### 🔍 Endpoints
- **POST /generate_text**
   - Description: Generates text using OpenAI's models.
   - Request Body:
     ```json
     {
       "model": "text-davinci-003", // OpenAI model to use
       "prompt": "Write a short story about a cat", // Text prompt
       "temperature": 0.7 // Controls randomness of the generated text
     }
     ```
   - Response:
     ```json
     {
       "response": "Once upon a time, in a cozy little cottage..." // The generated text
     }
     ```

### 🔒 Authentication
- This MVP does not implement user authentication. It is designed to be used with a single OpenAI API key stored in the environment variable.

### 📝 Examples
[See examples above]

## 📜 License & Attribution

### 📄 License
This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP
This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: OpenAI-Request-Wrapper-Backend

### 📞 Contact
For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="">
  <img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="">
  <img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="">
  <img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="">
</div>