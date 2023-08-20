Intern-Project

# Reddit Articles App

A web application to fetch and display Reddit thread data using Django (backend) and React (frontend).

## Backend (Django)

### Setup


1.  Locate into the project:
   ```bash
   cd backend
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Locate into the bakcend
   ```bash
   cd mysite
   ```
4. Create a Reddit app to obtain `client_id`, `uaer_agent` and `client_secret` Replace them in `myapp/views.py`.

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```



### Run

1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
2. Access the API endpoint at `http://localhost:8000/get_threads/` to fetch Reddit thread data in JSON format.

## Frontend (React)

### Setup

1. Install Node.js and npm on your system.

2. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

### Run

1. Start the React-Vite development server:
   ```bash
   npm run dev
   ```

2. Access the React app at `http://localhost:3000/` to see the fetched Reddit thread data displayed.

## Important Notes

- Make sure the Django backend is running before accessing the React frontend.
- Replace `'AskReddit'` with your desired subreddit name in the Django views.
- Handle API security and error handling based on your requirements.

---

You can copy and paste this README content into a file named `README.md` in the root directory of your project. Remember to customize any placeholders and paths according to your actual project structure and requirements.
