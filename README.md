# TaskMaster

TaskMaster is a robust web application built with Django and Django REST Framework. It allows users to create, update, and track tasks efficiently, featuring user authentication, RESTful APIs, and PostgreSQL for reliable data storage. Perfect for personal task management or as a learning project for Django development.

---

## Features

* **User Authentication**: Secure login and registration using Django AllAuth.
* **RESTful APIs**: Built with Django REST Framework for seamless task management.
* **Task Management**:

  * Create, update, and delete tasks.
  * Set task completion dates and track progress.
* **Database**: PostgreSQL for reliable and scalable data storage.
* **Customizable**: Easily extendable for additional features.

---

## Technologies Used

* **Backend**: Django, Django REST Framework
* **Database**: PostgreSQL
* **Authentication**: Django AllAuth, REST Framework Session Authentication
* **Frontend**: Django Templates (HTML, CSS)

---

## Installation

Follow these steps to set up TaskMaster locally:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Ahmed-zoubii/TaskMaster.git
   cd TaskMaster
   ```

2. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL**:

   * Make sure PostgreSQL is installed and running.
   * Create a database named `taskmaster`.
   * Update the `DATABASES` section in `settings.py` with your DB credentials.

5. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Admin)**:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

8. **Access the App**:
   Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API Endpoints

TaskMaster exposes a RESTful API. Here are a few key endpoints:

| Endpoint           | Method | Description             |
| ------------------ | ------ | ----------------------- |
| `/api/tasks/`      | GET    | List all tasks          |
| `/api/tasks/<id>/` | GET    | Retrieve a single task  |
| `/api/tasks/`      | POST   | Create a new task       |
| `/api/tasks/<id>/` | PUT    | Update an existing task |
| `/api/tasks/<id>/` | DELETE | Delete a task           |

Authentication is required for most endpoints. Token or session-based auth is supported.
