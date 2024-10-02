# 403dr0p3r

## Overview
`403dr0p3r` is a Python tool designed to bypass HTTP 403 Forbidden errors using various URL manipulation and header modification techniques. 
![403dr0p3r](/logo.png)

## Disclaimer 
This tool is intended for educational purposes and should only be used with permission on authorized systems.

## Features
- URL manipulation techniques to access restricted resources.
- Header modification techniques to bypass restrictions.
- Support for TRACE HTTP method.
- Wayback Machine integration to check archived snapshots.

## Installation

### Prerequisites
Make sure you have Python 3 installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the repository
```bash
git clone https://github.com/0xgh057r3c0n/403dr0p3r.git
cd 403dr0p3r
```

### Install dependencies
Use the provided `requirements.txt` file to install the necessary packages:
```bash
pip install -r requirements.txt
```

## Usage
To run the tool, execute the following command in your terminal:
```bash
python3 403dr0p3r.py
```

### Steps:
1. **Enter the Target URL**: Provide the target website URL (e.g., `https://example.com`).
2. **Enter the Path**: Specify the resource path you want to access (e.g., `images`).
3. **Review Output**: The tool will attempt various techniques to bypass the 403 error and display the results.

## Techniques Used
- URL Manipulation:
  - URL encoding (e.g., `%2e/`)
  - Path traversal attempts (e.g., `..;/`)
- Header Modification:
  - Custom headers like `X-Original-URL` and `X-Forwarded-For`.

## Disclaimer
This tool is for educational purposes only. Always obtain permission before testing the security of any system. Unauthorized access to systems is illegal and unethical.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please reach out to the author at [gauravbhattacharjee54@gmail.com](mailto:gauravbhattacharjee54@gmail.com).
