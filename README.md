# GitHub Release Notes Generator

Do you like to have the auto generated release notes for your GitHub repository? But are you too lazy to work in branches on your own projects? Then this is the tool for you! This tool will generate release notes for your repository based on the commits in the main branch.

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Supported versions">
  <img src="https://img.shields.io/github/license/StephanAkkerman/release-notes-generatorsvg?color=brightgreen" alt="License">
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
</p>

---

## Installation ⚙️

There are two methods to run this code. The first method is to run the Python code locally. The second method is to run the workflow in your GitHub repository to generate the release notes automatically.

### Method 1: Run the Python code locally

The required packages to run this code can be found in the requirements.txt file. To run this file, execute the following code block after cloning the repository:

```bash
pip install -r requirements.txt
```

### Method 2: Run the workflow in your GitHub repository

Simply copy the contents of the `.github/workflows/release_notes.yml` file to the `.github/workflows` directory in your repository. This will automatically generate the release notes for your repository, if you run the action. You can then copy paste the output to the release notes of your repository.

## Configuration ⚙️

For the Python code, you can configure the following settings in the `example.env` file:

- `GITHUB_TOKEN`: The GitHub token to access the GitHub API. You can create a token [here](https://github.com/settings/tokens/new)
- `REPO_OWNER`: The owner of the repository
- `REPO_NAME`: The name of the repository

## Usage 🚀

To run the Python code, execute the following code block:

```python
python main.py
```

## Example 📊

The following example shows the output of the release notes generator:

```markdown
# Release Notes

- #575 Add isort & black worfklow + pyproject.toml (closed on 2024-05-31)
- #573 Fix crypto TV ideas (closed on 2024-06-05)
- #568 Add cryptomoonshot subreddit (closed on 2024-06-05)
- #540 Only use reaction text of quote tweet for sentiment (closed on 2024-05-25)
- #539 retweet with img text is too short (closed on 2024-05-25)
- #534 List of broken APIs / channels (closed on 2024-06-15)
- #532 Use twikit for follow and unfollow commands (closed on 2024-05-25)
- #510 Improve reddit video embed (closed on 2024-05-25)
- #499 Change liquidations API (closed on 2024-06-15)
- #334 $ES_F bug (closed on 2024-05-26)
- #310 Fix reply to tweet text + img (closed on 2024-05-25)
```
