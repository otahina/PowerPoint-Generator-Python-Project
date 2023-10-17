![banner](https://github.com/otahina/PowerPoint-Generator-Python-Project/assets/108225969/bfe8f796-3ffa-4c59-92f5-7624f6f9884f)

[![made-with-python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/otahina/PowerPoint-Generator-Python-Project.git)
[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/otahina)

<img src="https://img.shields.io/github/stars/otahina/PowerPoint-Generator-Python-Project.svg"> <img src="https://img.shields.io/github/forks/otahina/PowerPoint-Generator-Python-Project.svg">

## PowerPoint Generator: Your Gateway to Effortless Presentations 🚀

Dive into the ease of presentation creation with PowerPoint Generator, a smart web application crafted to automate 
PowerPoint presentations! 🌟 
This project is ripe for growth and eager for your contributions. Let's enhance its capability together! 😊

## Demo Highlights 🎬

https://github.com/otahina/PowerPoint-Generator-Python-Project/assets/108225969/82d98c7a-0244-4fed-8f6b-f6c994fd69e3

## Table of Contents 📋

1. [Features](#features)
2. [Inner Structure of the Project](#inner-structure-of-the-project-🧐)
3. [How to Contribute](#how-to-contribute-💛)

## Features 🎨

* **AI-Driven Content Creation**: Utilize the power of GPT-3.5 Turbo to generate slide content based on user's input.
* **Intelligent Slide Generation**: The tool intelligently proposes titles and content for each slide.
* **Customizable Themes**: Choose color themes for your presentation, giving it a personalized touch.
* **User-Friendly Interface**: Clear instructions and an intuitive design make the PowerPoint generation process seamless and straightforward.

## Inner Structure of the project 🧐

If you want to learn how to use the GPT API for creating PowerPoint presentations or understand how the project is 
organized, check out [CODE_STRUCTURE.md](docs/CODE_STRUCTURE.md). 
In this document, I explain the code and the relationships between different parts of the code.


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

On the [GitHub page for this repository](https://github.com/otahina/PowerPoint-Generator-Python-Project.git), click on the Button "**Fork**".

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
git clone https://github.com/<your-github-username>/PowerPoint-Generator-Python-Project.git
```

> This makes a local copy of the repository in your machine.
>
> ⚠️ **Replace \<your-github-username\>!**

</details>

---

<details>
<summary>
Step 4: Create your feature branch 
</summary>

Always keep your local copy of the repository updated with the original repository.
Before making any changes and/or in an appropriate interval, follow the following steps:

- **Method 1:** GitHub Desktop

Learn more about how to create new branch [here](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/making-changes-in-a-branch/managing-branches#creating-a-branch) and how to fetch and pull origin from/to your local machine [here](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/keeping-your-local-repository-in-sync-with-github/syncing-your-branch).

Learn more about how to fetch and pull origin from/to your local machine using **GitHub Desktop** [here](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/keeping-your-local-repository-in-sync-with-github/syncing-your-branch).

- **Method 2:** Git

Run the following commands **_carefully_** to update your local repository

```sh
# If you cloned a while ago, get the latest changes from upstream
git checkout <master>
git pull upstream <master>

# Make a feature branch (Always check your current branch is up to date before creating a new branch from it to avoid merge conflicts)
git checkout -b <branch-name>

```

</details>

---
<details>
<summary>
Step 5: Pull Request
</summary>

Go to the GitHub page of _your fork_, and **make a pull request**:

Read more about pull requests on the [GitHub help pages](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

I'll check your pull request. 

</details>

---

If you want to learn more about how to contribute, visit [CONTRIBUTING.md](docs/CONTRIBUTING.md).

## Setup the Secret Key and OpenAI Key 🔑

The application uses a secret key for session management and an OpenAI key for the GPT-3.5 Turbo API.
These keys are defined as environment variables, and you can easily set them up using the provided .env.example file.

1. Locate the file named .env.example in the project directory.
2. Copy the contents of .env.example into a new file named .env.
3. Replace the placeholder values with your actual keys:
   
```
SECRET_KEY=your_secret_key
OPENAI_KEY=your_openai_key
PEXELS_API_KEY=your_pexels_key
```

Here's a brief description of each key and how to obtain them:

**SECRET_KEY**: 🔐This is used for web application security such as session management. You can create your own secure, random string for this.

**OPENAI_KEY**: 🤖This is required to access the OPENAI API. Although there's a limitation with the free version, it's sufficient for trying out this web application on your local machine. You can obtain this key by creating an account on the https://platform.openai.com.

**PEXELS_API_KEY**: 🏞️ This key is used for the free image search API provided by Pexels. It's very useful for adding creative images to your presentations. You can get this key by creating a free account on the https://www.pexels.com/api
After registering, the API key is automatically generated for you.

## Community Discussions 🗣️
Have a question, idea, or want to contribute? Join us in [Discussions](https://github.com/otahina/PowerPoint-Generator-Python-Project/discussions)!

## Contributors ✨

<img src="https://github.com/otahina.png" width="50" height="50" alt="description">
<a href="https://github.com/otahina">Ota Hina</a>
<img src="https://github.com/gaganmanku96.png" width="50" height="50" alt="description">
<a href="https://github.com/gaganmanku96">Gagandeep Singh</a>


## License 📄

This project is licensed under the terms of the MIT license.




