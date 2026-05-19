import requests

domain = input("Enter domain (example.com): ")

subdomains = [
    "www",
    "mail",
    "ftp",
    "test",
    "dev",
    "admin",
    "api",
    "blog",
    "shop"
]

print("\n[+] Starting Subdomain Recon...\n")

for sub in subdomains:
    url = f"http://{sub}.{domain}"

    try:
        response = requests.get(url, timeout=3)

        status = response.status_code

        if status == 200:
            print("[LIVE] ", url)
        elif status == 403:
            print("[BLOCKED] ", url)
        else:
            print("[FOUND] ", url, "Status:", status)

    except requests.exceptions.RequestException:
        print("[DOWN] ", url)
