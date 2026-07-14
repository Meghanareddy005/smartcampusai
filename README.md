# SmartCampusAI

SmartCampusAI is a production-ready, modular, and responsive Streamlit application designed for academic campus environments. It integrates a secure, local JSON-based authentication system with a custom Glassmorphic administration dashboard and an AI Chat assistant (supporting both OpenAI and Gemini).

## Features

- **Modern Glassmorphism UI**: Beautiful CSS customization featuring responsive layouts, custom scrollbars, animated cards, and smooth transitions.
- **Dynamic Routing**: Uses modern Streamlit navigation to direct logged-in users to the Dashboard, Profile, or Settings, while routing non-authenticated users to Login/Registration pages.
- **Secure Authentication**: Uses `bcrypt` for password hashing and standard input validations (email formats, username uniqueness, password strengths) on registration.
- **Rich Dashboard**: Provides key stats cards (Total Users, Total Chats, API Status, and Active Day Tracking), visual charts, and a dynamic AI Chat interface.
- **AI Chat Integrator**: Connects securely to either Gemini or OpenAI depending on the provided key format, avoiding any hardcoded keys.
- **Light & Dark Theme Toggle**: Easily toggle interface styles from the Settings page.

---

## Directory Structure

```
SmartCampusAI/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── assets/
│      logo.png
│      background.jpg
│      style.css
│
├── data/
│      users.json
│      chat_history.json
│
├── pages/
│      dashboard.py
│      login.py
│      register.py
│      profile.py
│      settings.py
│
├── utils/
│      auth.py
│      database.py
│      api.py
│      helpers.py
│
└── components/
       navbar.py
       sidebar.py
       cards.py
```

---

## Installation & Setup

### 1. Clone or Copy the Repository
Place the folder on your local machine and open a terminal in that directory.

### 2. Set Up a Virtual Environment (Recommended)
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create or open the `.env` file in the root directory and add your API key:
```env
API_KEY=your_gemini_or_openai_api_key
```
*Note: If `API_KEY` is not configured, the chat system will display a warning and run in demonstration mode with automated mock responses.*

### 5. Run the Application
```bash
streamlit run app.py
```

---

## Deployment

### Deploying to Streamlit Cloud
1. Push the code to a public/private GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and connect your GitHub account.
3. Click "New app", choose the repository, branch, and set the entry file to `app.py`.
4. In the app settings under "Secrets", paste your environment variable:
   ```toml
   API_KEY = "your_actual_api_key_here"
   ```
5. Deploy!

### Deploying to Render or Railway
- Deploy as a python web app or container.
- Specify the start command:
  ```bash
  streamlit run app.py --server.port $PORT --server.address 0.0.0.0
  ```
- Set `API_KEY` in the environment variables configuration on Render/Railway dashboard.
