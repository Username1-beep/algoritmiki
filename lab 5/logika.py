import urllib.request
import re

def get_file_contents(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def get_wiki_contents(wiki_url):
    with urllib.request.urlopen(wiki_url) as response:
        html = response.read().decode()
    text = re.sub(r'<.*?>', '', html) # remove html tags
    text = re.sub(r'\n+', '\n', text) # replace multiple newlines with one
    return text

def get_plagiarism_percentage(text, wiki_text):
    pattern = r'\b(\w+\W+){2}\w+\b' # match any three consecutive words
    match = re.search(pattern, text)
    if match:
        plagiarism_text = match.group(0)
        overlap_chars_count = sum([len(word) for word in plagiarism_text if word in wiki_text])
        return overlap_chars_count / len(text) * 100
    else:
        return 0

if __name__ == '__main__':
    wiki_url = 'https://ru.wikipedia.org/wiki/%D0%9B%D0%BE%D0%B3%D0%B8%D0%BA%D0%B0'
    wiki_text = get_wiki_contents(wiki_url)
    test_file_path = 'Логика.txt'
    test_text = get_file_contents(test_file_path)
    plagiarism_percentage = get_plagiarism_percentage(test_text, wiki_text)
    print(f'Plagiarism percentage: {plagiarism_percentage:.2f}%')
