import requests
from bs4 import BeautifulSoup
import time
from plyer import notification
import random
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def check_website(url, search_text):
    afile = open("useragents.txt")
    headers = random_line(afile).rstrip()  # Random header for bypassing security checks on the website
    print(f"Header is: {headers}")
    try:
        response = requests.get(url, headers={'User-Agent': headers}, timeout=100)
        # print(f"Below is response error if exists ---  0000  ----")
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Search for the desired text in the parsed HTML (case-insensitive)
        # print(soup.get_text().lower())
        if search_text.lower() in soup.get_text().lower():
            return True
        else:
            print(f"{search_text} is not found ...")
    except Exception as e:
        print(f"Error: {e}")
    return False

def send_email(subject, body):
    try:
        sender_email = "khaleel.org@gmail.com"
        receiver_email = [
            "khaleel.org@gmail.com",
            "hk.jigar@gmail.com",
            "tmail.khalil@gmail.com",
            "khaleel.gcloud@gmail.com"
        ]
        password = "gdkp dcjy ycmr qqrz"

        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = ", ".join(receiver_email)
        message['Subject'] = subject + ' | ' + datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")

        # Add body to email
        message.attach(MIMEText(body, 'plain'))

        # Create a secure SSL context and login
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()

        logging.info(f"Email sent to {receiver_email} with subject: {subject}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")


def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )
    send_email(title, message)

def random_line(afile):
    lines = afile.readlines()
    return random.choice(lines)

def main():
    # url = "https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=isla&realmId=108&categoryId=1600"  # Replace with the URL of the website you want to monitor
    # url = "https://web.archive.org/web/20230205081917/https://service2.diplo.de/rktermin/extern/choose_categoryList.do?locationCode=isla&realmId=108"
    url = "https://service2.diplo.de/rktermin/extern/choose_categoryList.do?locationCode=isla&realmId=108&request_locale=en" # main visa appointment page
    search_text = "study"  # Replace with the text you want to search for
    while True:
        print(f"Checking for = {search_text}")
        if check_website(url, search_text):
            while True:
                notify("Winter appointmens are open", f"The Word '{search_text}' is now available on {url}")
                print("Winter Appointments are open, notifying via Email ...")
                time.sleep(5)

        # Check the website every 30 seconds (adjust as needed)
        print("\nGoing to sleep for 5 seconds")
        time.sleep(5)

if __name__ == "__main__":
    main()
