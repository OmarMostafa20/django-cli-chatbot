# Django CLI Chatbot

Welcome to the Django CLI Chatbot, a mystical application designed to engage users in meaningful conversation, gather their precious information, and assist them with their inquiries through the advanced capabilities of "blenderbot-400M-distill" and BART models, integrated within a Django framework.


## Introduction

This project unveils a CLI-based chatbot that leverages the power of "blenderbot-400M-distill" for natural language processing and "BART" for generating concise summaries, all within a Django application framework. Designed to simulate customer service interactions, it collects user information, handles inquiries, logs conversations, and distills them into summaries, enhancing the user experience with AI-driven insights.


## Setup and Installation

Embark on this journey by preparing your environment with the necessary components.

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

### Model Setup

The chatbot utilizes two significant AI models:

- **blenderbot-400M-distill** for generating responses: This model requires no additional setup other than what's provided by the `transformers` library. You can find more information about blenderbot-400M-distill [here](https://huggingface.co/facebook/blenderbot-400M-distill?text=Yeah%2C+I%27ve+looked+into+those+areas+as+well.+Nothing+seems+out+of+the+ordinary.+I%27m+starting+to+wonder+if+there+might+be+an+issue+with+the+plumbing+or+something).

- **BART** for summarization tasks: Similarly, it's accessed via the `pipeline` function from `transformers`, focusing on summarizing user conversations. More details about the BART model can be found [here](https://huggingface.co/facebook/bart-large-cnn?text=%22Hey+there%21+I%27ve+been+having+some+issues+at+home+and+thought+I%27d+reach+out+for+some+advice.+Well%2C+recently+I%27ve+noticed+a+strange+odor+in+one+of+the+rooms%2C+and+I+can%27t+figure+out+where+it%27s+coming+from.+It%27s+been+bothering+me+for+a+while+now.+I%27ve+checked+everywhere%2C+from+the+kitchen+to+the+bathroom%2C+but+no+luck.+It%27s+not+a+typical+smell+like+rotten+food+or+a+leak.+It%27s+just+odd.%22).


### Database Configuration

1. Create a new database named `chatbot_db`.
2. Update `settings.py` with your database credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chatbot_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost', # Or your MySQL server IP
        'PORT': '3306',
    }
}
```

3. Apply migrations:

```python
python manage.py makemigrations
python manage.py migrate
```

## Usage

Engage with the chatbot through the terminal:

```python
python manage.py chat
```

Interact with the chatbot, provide your information, and explore its functionalities. The chatbot now supports summarizing user messages, utilizing the BART model for enhanced comprehension and summarization.

## Testing

Ensure the application's integrity:

```python
python manage.py test
```

This invokes tests verifying the application's functionalities, including model integrity and input handling.

