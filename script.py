import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

def check_website(url, search_text):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        session = requests.Session()
        response = session.get(url, headers=headers)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Search for the desired text in the parsed HTML (case-insensitive)
        if search_text.lower() in soup.get_text().lower():
            return True
        else:
            print("not found")
    except Exception as e:
        print(f"Error: {e}")
    return False

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

def main():
    url = "https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=isla&realmId=108&categoryId=1600"  # Replace with the URL of the website you want to monitor
    search_text = "summer"  # Replace with the text you want to search for

    while True:
        print("Checking for =", search_text)
        if check_website(url, search_text):

            while True:
                notify("Text Found", f"The text '{search_text}' is now available on {url}")        
                print("found")
                time.sleep(5)

        # Check the website every 30 seconds (adjust as needed)
        print("Going to sleep for 30 seconds")
        time.sleep(30)

if __name__ == "__main__":
    main()