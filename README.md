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

https://github.com/otahina/PowerPoint-Generator-Python-Project/assets/108225969/2ccee5da-6b75-412b-9c0a-b32b2e0966ba


The video is fast forwarded

## Getting Started! 🚀

To get a local copy up and running follow these steps:

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

4. **Run the application!**

```
python3 flaskapp.py
```
Make sure you set up the API key below first🙂

## Setup the Secret Key and OpenAI Key 🔑


1. The application uses a secret key for session management and an OpenAI key for the GPT-3.5 Turbo API.

You need to set these as environment variables in your terminal. On **Unix/Linux/macOS**, you can do this with the 'export' command:

```
export SECRET_KEY=your_secret_key
export OPENAI_KEY=your_openai_key
export PEXELS_API_KEY=your_pexels_key
```
Here's a brief description of each key and how to obtain them:

**SECRET_KEY**: 🔐This is used for web application security such as session management. You can create your own secure, random string for this.

**OPENAI_KEY**: 🤖This is required to access the OPENAI API. Although there's a limitation with the free version, it's sufficient for trying out this web application on your local machine. You can obtain this key by creating an account on the https://platform.openai.com.

**PEXELS_API_KEY**: 🏞️ This key is used for the free image search API provided by Pexels. It's very useful for adding creative images to your presentations. You can get this key by creating a free account on the https://www.pexels.com/api
After registering, the API key is automatically generated for you.

On **Windows**, you can do this with the 'set' command:

```
set SECRET_KEY=your_secret_key
set OPENAI_KEY=your_openai_key
set PEXELS_API_KEY=your_pexels_key
```
⚠️ Note that these environment variables will only be set for the duration of the terminal session. If you close the terminal and open a new one, you will need to set them again.

## How to contribute 💛

<details>
<summary>
Step 1: Star The Repo
</summary>

Star the repo to start your contribution ⭐️

![star repo](https://docs.github.com/assets/images/help/stars/starring-a-repository.png)

</details>

---

<details>
<summary>
Step 2: Fork it
</summary>

On the [GitHub page for this repository](https://github.com/ndleah/python-mini-project), click on the Button "**Fork**".

![fork image](https://upload.wikimedia.org/wikipedia/commons/3/38/GitHub_Fork_Button.png)

</details>

---

## License 📄

This project is licensed under the terms of the MIT license.




