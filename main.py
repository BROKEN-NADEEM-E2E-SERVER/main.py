import requests
import re
import time
import json
from bs4 import BeautifulSoup

SESSION = requests.Session()
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; vivo 1906) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
}


def login(email, password):
    login_page = SESSION.get("https://mbasic.facebook.com/login", headers=HEADERS)
    soup = BeautifulSoup(login_page.text, "html.parser")
    inputs = soup.find_all("input")

    data = {}
    for i in inputs:
        name = i.get("name")
        value = i.get("value")
        if name:
            data[name] = value

    data["email"] = email
    data["pass"] = password

    response = SESSION.post("https://mbasic.facebook.com/login/device-based/regular/login/", data=data, headers=HEADERS, allow_redirects=True)

    if "c_user" in SESSION.cookies.get_dict().keys():
        print("\nLOGIN SUCCESSFULLY 😈🔥")
        return True
    else:
        print("\nLOGIN FAILED ❌ Wrong Password or Checkpoint!")
        return False


def get_cookies():
    cookies = ";".join([f"{key}={value}" for key, value in SESSION.cookies.get_dict().items()])
    return cookies


def generate_token(cookies):
    url = "https://business.facebook.com/business_locations"
    HEADERS["Cookie"] = cookies
    result = SESSION.get(url, headers=HEADERS).text

    token = re.search(r'EAAG\w+', result)
    if token:
        return token.group(0)
    else:
        return None


def main():
    print("\n===============================")
    print("🔥 FACEBOOK TOKEN GENERATOR 🔥")
    print("===============================\n")

    email = input("📩 Enter Gmail: ")
    password = input("🔑 Enter Password: ")

    print("\n⏳ Logging In, Please Wait...")
    time.sleep(2)

    if login(email, password):
        cookies = get_cookies()
        print("\n🍪 Cookies Extracted:\n")
        print(cookies)

        print("\n⏳ Generating Token...")
        time.sleep(2)

        token = generate_token(cookies)

        if token:
            print("\n🎉 TOKEN SUCCESSFULLY GENERATED 🔥🔥")
            print("\nYour EAAD Token:\n")
            print(token)
        else:
            print("\n❌ Token Not Found! Maybe Account Locked or No Permission.")


if __name__ == "__main__":
    main()
