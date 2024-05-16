# Website Monitoring Script

This script monitors a specified website for the presence of a particular text and sends a desktop notification when the text is found. It uses random user-agent headers to bypass security checks on the website.

## Features

- Periodically checks a website for a specific text.
- Uses random user-agent headers from a file (`useragents.txt`) to avoid detection by security mechanisms.
- Sends desktop notifications when the specified text is found.
- Includes error handling and logging.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `plyer` library

## Installation

1. Install the required Python packages:
    ```bash
    pip install requests beautifulsoup4 plyer
    ```

2. Create a `useragents.txt` file in the same directory as your script. This file should contain different user-agent strings, one per line.

3. Download or clone the script.

## Usage

1. Modify the `url` and `search_text` variables in the script to your desired values.
    ```python
    url = "https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=isla&realmId=108&categoryId=1600"
    search_text = "language course"
    ```

2. Run the script:
    ```bash
    python3 your_script_name.py
    ```

Replace `your_script_name.py` with the name of your Python file.

## Script Details

The script performs the following steps:
1. Reads a random user-agent header from `useragents.txt`.
2. Sends an HTTP GET request to the specified URL using the random user-agent header.
3. Parses the HTML content of the page and searches for the specified text.
4. Sends a desktop notification if the text is found.
5. Repeats the check every 30 seconds.

### Example `useragents.txt`
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0
