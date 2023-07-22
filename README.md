![Banner Image](./for_readme/banner.png)

[![made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/otahina/PowerPoint-Generator-Python-Project.git)
[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/otahina)

## PowerPoint Generator is a smart web application that automates the creation of PowerPoint presentations.

This is my first open-source project as a computer science student. 😀
There are so many things for improvements in this web app, so please feel free to contribute to and kindly give me some advice! 😊
(Less emoji or something...🙄)

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

On the [GitHub page for this repository]([https://github.com/ndleah/python-mini-project](https://github.com/otahina/PowerPoint-Generator-Python-Project.git)), click on the Button "**Fork**".

![fork image](https://upload.wikimedia.org/wikipedia/commons/3/38/GitHub_Fork_Button.png)

</details>

---


<details>
<summary>
Step 3: Clone it
</summary>

- **Method 1:** GitHub Desktop

> ⚠️ **NOTE:** If you're not familiar with Git, using **GitHub Desktop Application** is a better start. If you choose this method, make sure to download it before continuing reading.
>
> ❗❗ Access link to download [**here**](https://desktop.github.com).

- **Method 2:** Git

Clone the forked repository. Open git bash and type:

```bash
git clone https://github.com/<your-github-username>/python-mini-project.git
```

> This makes a local copy of the repository in your machine.
>
> ⚠️ **Replace \<your-github-username\>!**

Learn more about [forking](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) and [cloning a repo](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

</details>

---

## License 📄

This project is licensed under the terms of the MIT license.




