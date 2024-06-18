from datetime import datetime

import requests


def load_env_file(file_path: str) -> dict:
    """
    Load environment variables from a .env file into a dictionary.

    Args:
    file_path (str): The path to the .env file.

    Returns:
    dict: A dictionary containing the environment variables.
    """
    env = {}
    with open(file_path, "r") as fp:
        for line in fp:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                key = key.strip().replace('"', "").replace("'", "")
                value = value.strip().replace('"', "").replace("'", "")
                env[key] = value
    return env


def fetch_latest_release():
    url = f"https://api.github.com/repos/{env['REPO_OWNER']}/{env['REPO_NAME']}/releases/latest"
    headers = {
        "Authorization": f"token {env['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def fetch_closed_issues(since):
    url = f"https://api.github.com/repos/{env['REPO_OWNER']}/{env['REPO_NAME']}/issues"
    headers = {
        "Authorization": f"token {env['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github.v3+json",
    }
    params = {"state": "closed", "since": since, "per_page": 100}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def generate_release_notes(issues):
    release_notes = []
    for issue in issues:
        if "pull_request" not in issue:  # Exclude pull requests
            title = issue["title"]
            number = issue["number"]
            closed_at = issue["closed_at"]
            formatted_date = datetime.strptime(
                closed_at, "%Y-%m-%dT%H:%M:%SZ"
            ).strftime("%Y-%m-%d")
            release_notes.append(f"- #{number} {title} (closed on {formatted_date})")

    return "\n".join(release_notes)


def save_release_notes(release_notes):
    with open("RELEASE_NOTES.md", "w") as file:
        file.write("# Release Notes\n\n")
        file.write(release_notes)


def main():
    latest_release = fetch_latest_release()
    closed_issues = fetch_closed_issues(latest_release["published_at"])
    release_notes = generate_release_notes(closed_issues)
    save_release_notes(release_notes)
    print("Release notes generated and saved to RELEASE_NOTES.md")


if __name__ == "__main__":
    env = load_env_file(".env")
    main()
