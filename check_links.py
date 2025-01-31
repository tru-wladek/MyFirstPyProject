import re
import requests


def extract_links(text):
    """Extracts all URLs from a given text using regex."""
    url_pattern = r"https?://[^\s]+"
    return re.findall(url_pattern, text)


def check_link_status(url):
    """Helps to mimic a real browser"""
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException:
        return "Error"

def read_text_file(file_path):
    """Reads the content of a text file and returns it as a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def main():
    file_path = "/Users/user/Desktop/links_to_check.txt"
    text = read_text_file(file_path)
    links = extract_links(text)
    i = 0

    for link in links:
        status = check_link_status(link)
        print(f"{i} URL: {link} - Status: {status}")
        i += 1


if __name__ == "__main__":
    main()