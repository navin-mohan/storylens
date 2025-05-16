# 📚 StoryLens – AI-Powered Story Library Manager
StoryLens is a full-stack single-page web application built using **Django Rest Framework, React.js, and Google Gemini API**. It allows users to **add, organize, and semantically search** a library of stories enhanced by AI-generated summaries and embeddings.

## ✨ Features
1. **Add New Stories:**
Users can create and manage their own story entries through a clean and intuitive React frontend.

2. **AI-Generated Summaries**: Upon submission, the story is processed using the Google Gemini API, which returns a concise, context-aware summary.

3. **Semantic Embeddings:** Each story is embedded using AI-generated vector representations to support semantic similarity search.

4. **Semantic Search Engine:** Users can search with a phrase or idea — not just keywords — and get ranked results based on semantic relevance.

## 🛠️ Tech Stack
### Frontend
- ⚛️ React.js (SPA with hooks and functional components)
- 🎨 HTML5, CSS3, JavaScript (ES6+)
- 🧪 Testing with Jest

### Backend
- 🐍 Python 3.11
- 🧰 Django + Django Rest Framework
- 🧪 Pytest for backend unit testing
- 🛢️ PostgreSQL (pgvector extension is used for vector embedding search)
- 📦 Custom RESTful API endpoints for AI integration and story management

### AI & Cloud
- 🤖 Google Gemini API (for summaries and embeddings)


## 🧪 Running Locally

```bash
# Clone the repository
git clone https://github.com/navin-mohan/storylens.git
cd storylens

# Backend setup
cd backend
pip install -r requirements.txt

# Create a .env file to hold the API key and database credentials
touch .env
```

Add the following to the `.env` file:

```bash
GEMINI_API_KEY="<YOUR API KEY>"
POSTGRES_DB="<YOUR DATABASE NAME"
POSTGRES_USER="<YOUR DATABASE USERNAME>"
POSTGRES_PASSWORD="<YOUR DATABASE PASSWORD>"
POSTGRES_HOST="<YOUR DATABASE HOSTNAME>"
POSTGRES_PORT="<YOUR DATABASE PORT>"
```

Start the application.

```bash
python manage.py migrate
python manage.py runserver

# Frontend setup
cd ../frontend
npm install
npm run dev

```