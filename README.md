# Django CLI Chatbot

Welcome to the Django CLI Chatbot, a mystical application designed to engage users in meaningful conversation, gather their precious information, and assist them with their inquiries through the power of Flan-T5 and the Django framework.

## Introduction

This project conjures a CLI-based chatbot that utilizes the advanced capabilities of Flan-T5 for natural language processing, integrated within a Django application framework. It's designed to simulate a customer service interaction, where it collects user information, handles inquiries, and logs conversations. Complaints are distilled into summaries, each adorned with a unique ID for future reference.

## Setup and Installation

To embark on this journey, you must prepare your environment with the necessary incantations and components.

### Prerequisites

- Python 3.8 or higher
- pip and virtualenv
- MySQL Server

### Environment Setup

1. Clone the repository to your local domain:

```bash
git clone <repository-url>
```

2. Venture into the project directory:

```bash
cd chatbot_project
```

3. Conjure a virtual environment and activate it:

- On Windows:
  ```bash
  python -m venv env
  env\\Scripts\\activate
  ```
- On macOS and Linux:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

4. Install the required spells (dependencies):

```python
pip install -r requirements.txt
```

### Database Configuration

1. Brew the MySQL potion to create a new database named `chatbot_db`.
2. Alter the `settings.py` to reflect your database credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chatbot_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

3. Perform the ancient ritual of migrations:

```python
python manage.py makemigrations
python manage.py migrate
```

## Usage

To awaken the chatbot, perform the following incantation in your terminal:

```python
python manage.py chat
```

Follow the prompts to engage in conversation, provide your information, and explore the functionalities of the chatbot.

## Testing

To ensure the integrity of the spells and components, run the following command:

```python
python manage.py test
```

This will invoke the tests written to verify the application's functionalities, including model integrity, command input handling, and data validation.


## Contribution

Contributions are welcomed from all corners of the realm. To contribute:

1. Fork the repository.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -am 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a Pull Request.

Please ensure your contributions adhere to the project's coding style and standards. All spells and incantations should be thoroughly tested before submission.