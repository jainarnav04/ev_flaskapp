# EV Flask App

A Flask web application with Firebase integration, ready for deployment on Render.

## Features
- User authentication (login/register)
- Google Firebase Firestore integration
- Responsive dashboard and login templates

## Setup
1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your Firebase service account JSON (do NOT commit it!)
5. Set the environment variable:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/firebase.json
   ```
6. Run the app:
   ```bash
   flask run
   ```

## Deployment (Render)
- Upload your Firebase JSON as a Secret File
- Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the secret file path
- Render will use the `Procfile` and `requirements.txt` for deployment

## Security
- Never commit secrets or `.env` files
- Use `.gitignore` to keep sensitive files out of version control
