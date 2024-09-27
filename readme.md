Here are the step-by-step commands for someone to run your project after cloning it:

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/siddu015/Tutor_AI.git>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd webbot_project
   ```

3. **Create a virtual environment (if not already created):**
   ```bash
   python -m venv env
   ```

4. **Activate the virtual environment:**
    - On Windows:
      ```bash
      env\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source env/bin/activate
      ```

5. **Install the required packages:**
   ```bash
   pip install django wolframalpha wikipedia-api
   ```

6. **Make migrations:**
   ```bash
   python manage.py makemigrations
   ```

7. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

Now, your project should be up and running!