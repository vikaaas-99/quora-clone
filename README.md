# 🧠 Quora Clone – Django Q&A Web App

A simple Q&A website inspired by Quora, built with Django.  
Users can register, log in, post questions, answer others’ questions, like answers, and log out.

---

## 🚀 Features

- 🔐 User Registration & Login
- ❓ Post Questions
- 📖 View All Questions
- ✍️ Answer Questions
- ❤️ Like Answers
- 👋 Logout
- 📋 Admin Interface with filters and search

---

## 🛠️ Tech Stack

- **Backend**: Django 4.x
- **Frontend**: HTML, Bootstrap 5 (CDN)
- **Database**: SQLite (default)

---

## 📂 Project Structure

```
quora_clone/
├── core/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── question_list.html
│   │   ├── post_question.html
│   │   └── question_detail.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── quora_clone/
│   └── settings.py
│   └── urls.py
└── manage.py
```

---

## 🧑‍💻 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/vikaaas-99/quora-clone.git
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install django
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 🛡️ Admin Panel

Access the Django admin at: [http://localhost:8000/admin](http://localhost:8000/admin)
