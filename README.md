![Banner Image](./for_readme/banner.png)

[![made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## PowerPoint Generator is a smart web application that automates the creation of PowerPoint presentations.

## Features 🎨


* **AI-Driven Content Creation**: Utilize the power of GPT-3.5 Turbo to generate slide content based on your input.
* **Intelligent Slide Generation**: The tool intelligently proposes titles and content for each slide.
* **Customizable Themes**: Choose color themes for your presentation, giving it a personalized touch.
* **User-Friendly Interface**: Clear instructions and an intuitive design make the PowerPoint generation process seamless and straightforward.
* **Secure Authentication**: Register and log in with peace of mind, as user information is securely stored.

## Demo Highlights 🎬

Comming soon!

## Getting Started! 😆



1. **Clone the repository**:

```
git clone otahina/PowerPoint-Generator-Python-Project
```

2. **Navigate to the project directory**:

```
PowerPoint-Generator-Python-Project
```

3. **Install the required Python packages. This project relies on several Python packages for its functionality**:


```
pip install flask flask_login flask_bcrypt flask_sqlalchemy python_dotenv python_pptx
```

## Setup the Secret Key and OpenAI Key 🔑


1. The application uses a secret key for session management and an OpenAI key for the GPT-3.5 Turbo API.

You need to set these as environment variables in your terminal. On **Unix/Linux/macOS**, you can do this with the 'export' command:

```
export SECRET_KEY=your_secret_key
export OPENAI_KEY=your_openai_key
```
Replace your_secret_key with a secure, random string. Replace your_openai_key with your personal OpenAI key.


On **Windows**, you can do this with the 'set' command:

```
set SECRET_KEY=your_secret_key
set OPENAI_KEY=your_openai_key
```
⚠️ Note that these environment variables will only be set for the duration of the terminal session. If you close the terminal and open a new one, you will need to set them again.


