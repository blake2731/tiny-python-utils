import re

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

if __name__ == "__main__":
    print(slugify("Hello World! This is GitHub"))
