import requests
from bs4 import BeautifulSoup
import re

def extract_email(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        script_data = soup.find_all('script')[15].text
        script_data = script_data.replace("\\n", "")
        script_data = script_data.replace("\\t", "")

        pattern = re.compile(r"\"emailAddress\":\"(.+?)\"")
        email = re.findall(pattern, script_data)

        if email:
            return email[0]
        else:
            return "Email not found"

    except Exception as e:
        return str(e)

# Use the function to extract the email from a LinkedIn profile URL
url = "https://www.linkedin.com/in/example-profile-123456/"
print(extract_email(url))
