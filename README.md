#     Working Proxy Checker Script

This Python script checks a list of proxy addresses from a file and identifies the working ones by testing them against a test URL. If a proxy responds successfully, it is considered a working proxy and added to the output file.

## Prerequisites

- Python (3.x recommended)
- `requests` library (install using `pip install requests`)

## Usage

1. git clone https://github.com/Jhon2Doe/WorkingProxyChecker.git

2. Create a file named `proxy.txt` in the same directory with a list of proxy addresses, each on a separate line.

   Example `proxy.txt` file:
xxx.xxx.xxx.xxx:8080
xxx.xxx.xxx.xxx:4145

3. Open a terminal/command prompt and navigate to the directory containing the script.

4. Run the script using the command:

```bash
python3 proxychecker.py

```

## Customization

You can replace the test URL http://ifconfig.io in the script with any other URL you want to use for testing proxy connectivity.
