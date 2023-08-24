import requests

def check_proxy(proxy):
    url = "http://ifconfig.io"
    proxies = {
        "http": proxy,
        "https": proxy
    }

    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        pass
    return False

def main():
    with open("proxy.txt", "r") as proxy_file:
        proxies = proxy_file.read().splitlines()

    working_proxies = []

    for proxy in proxies:
        if check_proxy(proxy):
            working_proxies.append(proxy)

    with open("working_proxies.txt", "w") as working_file:
        for proxy in working_proxies:
            working_file.write(proxy + "\n")

if __name__ == "__main__":
    main()
