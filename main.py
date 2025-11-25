import requests
import re

def generate_token_from_cookies(raw_cookie):
    try:
        cookies = {}
        for part in raw_cookie.split(';'):
            if '=' in part:
                name, value = part.strip().split('=', 1)
                cookies[name] = value

        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; Mobile) AppleWebKit/537.36 Chrome/103.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        url = "https://business.facebook.com/business_locations"

        response = requests.get(url, headers=headers, cookies=cookies)

        token = ""
        match = re.search(
            r'EAAG[A-Za-z0-9]+',
            response.text
        )
        if match:
            token = match.group(0)
        else:
            match = re.search(
                r'EAAB[A-Za-z0-9]+',
                response.text
            )
            if match:
                token = match.group(0)

        if token:
            return token
        else:
            return "❌ Token not found! Cookie invalid or expired."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"


if __name__ == "__main__":
    print("\n=== COOKIES → TOKEN GENERATOR BY BROKEN NADEEM ===\n")
    cookies = input("PASTE YOUR FB COOKIES: ")

    token = generate_token_from_cookies(cookies)
    print("\n--------------------------------------")
    print("TOKEN RESULT:")
    print(token)
    print("--------------------------------------")
