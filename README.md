# CodeConverto
converts your favorite programming language into different language

### Installation

To install code converto and it locally paste this into your terminal:

```bash
// installing requirements
pip install -r requirements.txt

//run into your local machine
flask --app app run
```
If you run into problems while running it locally, especially when installing openai, openai requires you to upgrade by running `pip install --upgrade openai`, then initialize grit with `grit init`, install the latest update with `grint install --update`, then migrate with `openai migrate`.

#### Automatic migration with grit on Window

To use grit to migrate your code on Windows, you will need to use Windows Subsystem for Linux (WSL). Installing WSL is quick and easy, and you do not need to keep using Linux once the command is done.

Here's a step-by-step guide for setting up and using WSL for this purpose:

Open a PowerShell or Command Prompt as an administrator and run wsl --install.
- Restart your computer.
- Open the WSL application.
- In the WSL terminal, cd into the appropriate directory `(e.g., cd /mnt/c/Users/Myself/my/code/)` and then run the following commands:
```
curl -fsSL https://docs.grit.io/install | bash
grit install
grit apply openai
```

You can also specify the environment variables in your Flask app by modifying the .flaskenv. It is important to create a .env file for your OpenAI secret key; you can find it [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-api-key)

```bash
// .flaskenv
FLASK_ENV = development
FLASK_APP = app.py
FLASK_DEBUG = True

// .env (create newfile)
OPENAI_API_KEY = your secret key here
```

### Issues

If you're having trouble integrating this code into your machine, [open a new issue](https://github.com/kents00/CodeConverto/issues). As this repository continues to develop, it will be easier for more developers to integrate updates and improve overall user performance!
