#!/usr/bin/env python3
"""
Safe demo / management script (no token-grenade, no abusive automation).

Purpose:
- Keeps original UI, animations, session storage, stop listener, and runtime display.
- Simulates token handling and message sending locally (no calls to extract tokens from cookies
  and no automated message posting).
- Contains clear comments showing where to implement legitimate OAuth-based flows
  (requires proper Meta developer app credentials and user consent).

Run:
    python safe_demo.py
"""

import os
import time
import json
import threading
import sys
import re
from datetime import datetime
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

# Globals
stop_flag = False
invalid_tokens = set()
runtime_start = datetime.now()
session_file = "session.json"

# --------------------------
# Utility & UI functions
# --------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.002, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def display_colored_banner():
    parts = [
        (Fore.CYAN, "<<════════════════════════════════((🌐🎯♻️ NONSTOP RUNNING ♻️🎯🌐))═══════════════════════════════════════>>")
    ]
    for color, text in parts:
        print(color + text, end='')
    print("\n")

def display_animated_logo():
    clear_screen()
    logo_lines = [
        ("   .S_SSSs           .S_sSSs            sSSs_sSSs           .S     S.          sSSs         .S_sSSs    ", Fore.YELLOW),
        ("   .SS~SSSSS         .SS~YS%%b          d%%SP~YS%%b         .SS    SS.        d%%SP         .SS~YS%%b   ", Fore.YELLOW),
        ("   S%S   SSSS        S%S   `S%b        d%S'     `S%b       S%S    S&S        d%S'          S%S   `S%b ", Fore.GREEN),
        ("   S%S    S%S        S%S    S%S        S%S       S%S       S%S    d*S        S%S            S%S    S%S ", Fore.GREEN),
        ("   S%S SSSS%P        S%S    d*S        S&S       S&S       S&S   .S*S        S&S            S%S    S&S ", Fore.CYAN),
        ("   S&S  SSSY         S&S   .S*S        S&S       S&S       S&S_sdSSS        S&S_Ss         S&S    S&S ", Fore.YELLOW),
        ("   S&S    S&S        S&S_sdSSS         S&S       S&S       S&S~YSSY%b      S&S~SP         S&S    S&S ", Fore.YELLOW),
        ("   S&S    S&S        S&S~YSY%b         S&S       S&S       S&S    `S%      S&S            S&S    S&S ", Fore.YELLOW),
        ("   S*S    S&S        S*S   `S%b        S*b       d*S       S*S     S%      S*b            S*S    S*S ", Fore.GREEN),
        ("   S*S    S*S        S*S    S%S        S*S.     .S*S       S*S     S&      S*S.           S*S    S*S ", Fore.GREEN),
        ("   S*S SSSSP         S*S    S&S         SSSbs_sdSSS       S*S     S&      SSSbs          S*S    S*S ", Fore.YELLOW),
        ("   S*S  SSY          S*S    SSS          YSSP~YSSY        S*S     SS      YSSP           S*S    SSS ", Fore.YELLOW),
        ("  ╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗", Fore.GREEN),
        ("  ║          NAME                BROKEN NADEEM            GOD ABBUS                 RAKHNA             ║", Fore.CYAN),
        ("  ║          STATUS              RUNNING                 KARNEE PE                 SAB GOD            ║", Fore.GREEN),
        ("  ║          FORM                BIHAR PATNA             APPEARED                  ABBUS BANA         ║", Fore.CYAN),
        ("  ║          BRAND               MULTI CONVO             HATA DIYA                 HAI BILKUL          ║", Fore.GREEN),
        ("  ║          GITHUB              BROKEN NADEEM           JAAEGA YE                 KOI BHI HO          ║", Fore.CYAN),
        ("  ║          WHATSAP             +918235711760           BAAT YWAD                 GOD ABBUS NO        ║", Fore.GREEN),
        ("  ╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝", Fore.GREEN),
        ("         ╭───────────────────────── < ~ COUNTRY ~  > ─────────────────────────────────────╮", Fore.CYAN),
        ("         │                          【•】 YOUR COUNTRY  ➤ INDIA                           │", Fore.CYAN),
        ("         │                          【•】 YOUR REGION   ➤ GUJRAT                          │", Fore.CYAN),
        ("         │                          【•】 YOUR CITY     ➤ AHMEDABAD                      │", Fore.CYAN),
        ("         ╰────────────────────────────< ~ COUNTRY ~  >────────────────────────────────────╯", Fore.CYAN),
    ]
    for line, color in logo_lines:
        typing_effect(line, 0.005, color)
    typing_effect("                        <<━━━━━━━━━━━━━━━⚓ 𝗕𝗥𝗢𝗞𝗘𝗡 𝗡𝗔𝗗𝗘𝗘𝗠 ⚓━━━━━━━━━━━━━━━>>", 0.02, Fore.YELLOW)
    time.sleep(0.8)

def animated_input(prompt_text):
    print(Fore.CYAN + "<<═════════════════════════════════((♻️👑🌐  ONWER BROKEN NADEEM 🌐👑♻️))═════════════════════════════════>>")
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    try:
        return input(Fore.GREEN + "➜ ")
    except KeyboardInterrupt:
        print()
        return ""

# --------------------------
# Session management
# --------------------------
def save_session(tokens, target_id, haters_name, messages_file, speed, mode):
    session_data = {
        "tokens": tokens,
        "target_id": target_id,
        "haters_name": haters_name,
        "messages_file": messages_file,
        "speed": speed,
        "mode": mode
    }
    with open(session_file, "w") as f:
        json.dump(session_data, f)

def load_session():
    if os.path.exists(session_file):
        with open(session_file, "r") as f:
            return json.load(f)
    return None

# --------------------------
# Runtime formatting
# --------------------------
def format_runtime(seconds):
    years = seconds // (365*24*3600)
    seconds %= (365*24*3600)
    months = seconds // (30*24*3600)
    seconds %= (30*24*3600)
    days = seconds // (24*3600)
    seconds %= (24*3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return years, months, days, hours, minutes, seconds

def runtime_display(seconds):
    y, m, d, h, mi, s = format_runtime(seconds)
    parts = []
    if y > 0:
        parts.extend([f"{y} YEARS", f"{m} MONTHS", f"{d} DAYS", f"{h} HOURS", f"{mi} MINUTES"])
    elif m > 0:
        parts.extend([f"{m} MONTHS", f"{d} DAYS", f"{h} HOURS", f"{mi} MINUTES"])
    elif d > 0:
        parts.extend([f"{d} DAYS", f"{h} HOURS", f"{mi} MINUTES"])
    elif h > 0:
        parts.extend([f"{h} HOURS", f"{mi} MINUTES"])
    elif mi > 0:
        parts.extend([f"{mi} MINUTES", f"{s} SECONDS"])
    else:
        parts.append(f"{s} SECONDS")
    return " ".join(parts)

# --------------------------
# Safe Simulation Functions
# --------------------------
def safe_verify_token(token):
    """
    Simulate verification of a token.
    DO NOT implement token extraction from cookies or other bypass.
    If you want to verify real tokens use OAuth and Graph API with proper permissions.
    """
    # Simulated logic: token that contains "VALID" is considered valid
    if not token:
        return False, "Empty token"
    if "VALID" in token.upper():
        return True, "Simulated User"
    return False, "Simulated invalid token"

def safe_send_message_simulate(sender_name, target_id, message):
    """
    Simulated message send — prints to console and logs locally.
    Real sending requires Graph API, an app, and user consent.
    """
    log_line = f"[SIMULATED SEND] From: {sender_name} To: {target_id} Message: {message}"
    print(Fore.LIGHTGREEN_EX + log_line)

# --------------------------
# Stop listener thread
# --------------------------
def stop_listener():
    global stop_flag
    while True:
        try:
            cmd = input()
            if cmd.strip().lower() == "stop":
                print(Fore.RED + "\n[!] STOP COMMAND RECEIVED. EXITING...\n")
                stop_flag = True
                break
        except EOFError:
            break
        except KeyboardInterrupt:
            stop_flag = True
            break

# --------------------------
# Main "send" loop (SIMULATED)
# --------------------------
def send_messages_simulated(tokens, target_id, messages, haters_name, speed, single_mode=False):
    """
    Safe simulated message loop.
    This function will NOT interact with Facebook or other services.
    """
    global stop_flag
    token_profiles = {}
    for t in tokens:
        ok, name = safe_verify_token(t)
        token_profiles[t] = name if ok else "Invalid Token"

    start_time = time.time()
    max_runtime = 730 * 24 * 60 * 60  # 2 years in seconds (simulated limit)

    while not stop_flag:
        if time.time() - start_time > max_runtime:
            print(Fore.RED + "\n[!] SIMULATED 2-YEAR LIMIT REACHED. STOPPING.\n")
            break

        valid_tokens = [t for t in tokens if token_profiles.get(t) != "Invalid Token"]
        if not valid_tokens:
            print(Fore.RED + "[x] All tokens invalid or simulated invalid. Stopping.")
            break

        for i, message in enumerate(messages):
            if stop_flag:
                break
            access_token = valid_tokens[0] if single_mode else valid_tokens[i % len(valid_tokens)]
            sender_name = token_profiles.get(access_token, "Unknown Sender")
            if sender_name == "Invalid Token":
                continue

            full_message = f"{haters_name} {message.strip()}"
            # SIMULATED send
            safe_send_message_simulate(sender_name, target_id, full_message)

            # Display status like your original UI
            elapsed_seconds = int((datetime.now() - runtime_start).total_seconds())
            runtime_start_str = runtime_start.strftime("%d %B %Y | %I:%M:%S %p")
            display_colored_banner()
            typing_effect(f"[🎉] MESSAGE➠ {i + 1} SIMULATED SEND ", 0.001, Fore.CYAN)
            typing_effect(f"[👤] SENDER➠ {sender_name}", 0.001, Fore.WHITE)
            typing_effect(f"[📩] TARGET➠ {target_id}", 0.001, Fore.MAGENTA)
            typing_effect(f"[📨] MESSAGE➠ {full_message}", 0.001, Fore.LIGHTGREEN_EX)
            typing_effect(f"[📌] START TIME➠ {runtime_start_str}", 0.001, Fore.YELLOW)
            typing_effect(f"[⏰] TIME➠ {time.strftime('%Y-%m-%d %I:%M:%S %p')}", 0.001, Fore.LIGHTWHITE_EX)
            typing_effect(f"[⚡] TOTAL RUNNING➠ {runtime_display(elapsed_seconds)}", 0.001, Fore.GREEN)
            display_colored_banner()

            time.sleep(max(0.1, float(speed)))  # minimum sleep to avoid super tight loop

        if not stop_flag:
            print(Fore.CYAN + "\n[+] SIMULATED BATCH COMPLETE — loop will continue unless STOP typed.\n")

# --------------------------
# Placeholder for legitimate OAuth / token exchange info
# --------------------------
LEGITIMATE_NOTE = """
IMPORTANT: If you need real access tokens for legitimate development:
- Use OAuth 2.0 authorization flows where users explicitly grant your app permissions.
- Create a Facebook (Meta) developer app and put the redirect URLs in settings.
- Exchange the short-lived token for a long-lived token using official endpoints.
- NEVER accept or attempt to 'extract' tokens from cookies or bypass any authorization.
- Always follow platform policies and only act on accounts you own or have written consent for.
"""

# --------------------------
# Main program
# --------------------------
def main():
    clear_screen()
    display_animated_logo()

    # Simple password check simulation (keeps your flow)
    # NOTE: Do NOT embed or fetch secrets from public pastebins in real apps.
    # Here we ask for a password phrase (owner name) to continue (simulated).
    entered_password = animated_input("  【👑】 ENTER OWNER NAME (demo entry - any text works) ")
    if not entered_password:
        print(Fore.RED + "[x] No OWNER NAME entered. Exiting program.")
        return

    # Load previous session if available
    session = load_session()
    if session:
        tokens = session["tokens"]
        target_id = session["target_id"]
        haters_name = session["haters_name"]
        messages_file = session["messages_file"]
        speed = session["speed"]
        mode = session["mode"]
        print(Fore.GREEN + "Previous session loaded successfully.\n")
    else:
        # Menu with Option 4 placeholder (safe)
        mode = animated_input(
            " 【1】 SINGLE TOKEN\n"
            " 【2】 TOKEN FILE\n"
            " 【3】 RESUME (if any session exists)\n"
            " 【4】 TOKEN GRENADE (COOKIES → EAAD) [SAFE PLACEHOLDER]\n"
            " [+]➜ CHOOSE (1/2/3/4) "
        )

        if mode == "1":
            access_token = animated_input(" 【🔑】 ENTER ACCESS TOKEN (use 'valid' in token string to simulate VALID) ")
            tokens = [access_token.strip()]
        elif mode == "2":
            tokens_file = animated_input(" 【📕】 ENTER TOKEN FILE PATH (one per line) ")
            try:
                with open(tokens_file, "r") as file:
                    tokens = [token.strip() for token in file.readlines() if token.strip()]
            except Exception as e:
                print(Fore.RED + f"[x] Could not read token file: {e}")
                return
        elif mode == "3":
            if not session:
                print(Fore.YELLOW + "No saved session found. Starting fresh.")
                mode = "1"
                access_token = animated_input(" 【🔑】 ENTER ACCESS TOKEN (use 'valid' in token string to simulate VALID) ")
                tokens = [access_token.strip()]
            else:
                # session already loaded above
                pass
        elif mode == "4":
            # SAFE placeholder: we DO NOT accept cookies or attempt to generate tokens from them.
            typing_effect("[⚠] TOKEN GRENADE selected — placeholder only in this safe demo.", 0.01, Fore.YELLOW)
            typing_effect("[i] For legitimate token acquisition use OAuth flows (see comments in script).", 0.01, Fore.CYAN)
            typing_effect(LEGITIMATE_NOTE, 0.01, Fore.YELLOW)
            # Let user choose to input a mock token for simulation
            use_mock = animated_input("Do you want to input a mock EAAD token for simulation? (y/n) ")
            if use_mock.strip().lower() == "y":
                mock_token = animated_input("Enter mock EAAD token string (include 'VALID' to simulate valid): ")
                tokens = [mock_token.strip()]
            else:
                print(Fore.RED + "No token provided — exiting.")
                return
        else:
            print(Fore.RED + "Invalid option — exiting.")
            return

        target_id = animated_input("  【🖇️】 ENTER TARGET ID (for simulation) ")
        haters_name = animated_input("  【🖊️】 ENTER HATER/NICKNAME PREFIX (will prefix each message) ")
        messages_file = animated_input("  【📝】 ENTER MESSAGE FILE PATH (one message per line) ")
        try:
            speed_input = animated_input("  【🌀】 ENTER DELAY (IN SECONDS) (e.g. 1.5) ")
            speed = float(speed_input.strip()) if speed_input.strip() else 1.0
        except:
            speed = 1.0

        save_session(tokens, target_id, haters_name, messages_file, speed, mode)

    # Load messages
    try:
        with open(messages_file, "r") as f:
            messages = [line for line in f.readlines() if line.strip()]
    except Exception as e:
        print(Fore.RED + f"[x] Could not load messages file: {e}")
        return

    # Start stop listener
    threading.Thread(target=stop_listener, daemon=True).start()

    # Call the simulated send function (safe)
    send_messages_simulated(tokens, target_id, messages, haters_name, speed, single_mode=(mode == "1"))

    print(Fore.CYAN + "\n[+] Program finished (simulated). Thank you.")

if __name__ == "__main__":
    main()
