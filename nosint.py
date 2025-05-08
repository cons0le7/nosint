import os
import sys
import time
import json
import requests
import subprocess
from colorama import init, Fore, Style

base_url = "https://nosint.org/api/stream-search"
api_key = None
repo_url = "https://github.com/cons0le7/nosint"
home_path = os.environ['HOME']


banner = r"""
      _______          _________ ___ __________________
      \      \   ____ /   _____/|   |\      \__    ___/
 ━━━━━/   |   \ /  _ \\_____  \ |   |/   |   \|    |━━━━━
     /    |    (  <_> )        \|   /    |    \    |
     \____|__  /\____/_______  /|___\____|__  /____|
      ━══════\/══════════════\/═════════════\/════━
                                 nosint.org"""
menu = """
                ╔═════════════════════╗
                ║   [1] Search        ║
                ║   [2] Update Token  ║
                ║   [3] Update Tool   ║
                ║   [x] Exit          ║
                ╚═════════════════════╝
"""

def get_api_key():
    os.system("clear")
    print(banner)
    home_dir = os.path.expanduser("~")
    api_file_path = os.path.join(home_dir, ".nosint", "api.key")

    api_key = None

    nosint_dir = os.path.join(home_dir, ".nosint")
    if not os.path.exists(nosint_dir):
        try:
            os.makedirs(nosint_dir)
            print(f"\nCreated directory: {nosint_dir}")
        except OSError as e:
            print(f"\nError creating directory {nosint_dir}: {e}")
            pass

    if os.path.exists(api_file_path):
        try:
            with open(api_file_path, "r") as f:
                api_key = f.read().strip()
            if api_key:
                return api_key
            else:
                print("\n$HOME/.nosint/api.key file found but is empty.")
        except IOError as e:
            print(f"\nError reading $HOME/.nosint/api.key file: {e}.")

    print("\nAPI key not found in $HOME/.nosint/api.key or file was empty/unreadable.")
    api_key = input("\nPlease enter your API key: ").strip()
    if api_key:
        save_key = input(f"\nDo you want to save this API key for future use in {api_file_path}? (y/n): ").lower()
        if save_key == "y":
            try:
                with open(api_file_path, "w") as f:
                    f.write(api_key)
                print(f"\nAPI key saved to {api_file_path}.")
            except IOError as e:
                print(f"\nError saving API key to {api_file_path}: {e}")
        return api_key
    else:
        print("\nNo API key entered.")
        return None

def update_token():
    os.system("clear")
    print(banner)
    token_update_choice = input("\nUpdate token? (y/n): ").strip().lower()
    if token_update_choice == "y":
        new_api_key = input("\nPlease enter your new API key: ").strip()
        if new_api_key:
            try:
                api_key_path = os.path.join(os.environ['HOME'], 'nosint', 'api.key')
                os.makedirs(os.path.dirname(api_key_path), exist_ok=True)
                with open(api_key_path, "w") as f:
                    f.write(new_api_key)
                print("\nAPI key updated successfully.")
                global api_key
                api_key = new_api_key
            except IOError as e:
                print(f"\nError saving new API key: {e}")
        else:
            print("\nNo new API key entered.")
        input("\nPress Enter to return to the main menu...")
        main()
    else:
        main()

def update_tool():
    os.system("clear")
    print(banner)
    update_tool_choice = input("\nUpdate tool? (y/n): \n\n >>> ").strip().lower()
    if update_tool_choice == "y": 
        os.system("clear")
        print(banner)
        try:
            if not os.path.isdir(home_path):
                print("\n")
                subprocess.run(["git", "clone", repo_url, home_path], check=True)
                input("\nUpdate successful. Press Enter to close script. \n\n >>> ")
                sys.exit()
            else:
                print("\n")
                subprocess.run(["git", "-C", home_path, "pull"], check=True)
                input("\nUpdate successful. Press Enter to close script. \n\n >>> ")
                sys.exit()
        except subprocess.CalledProcessError as e:
            print(f"\nAn error occurred while updating tool: {e}")  
            input("\nAborting. Press enter to return to main menu. \n\n >>> ")
            main()
    else: 
        os.system("clear")
        print(banner)
        input("\nAborting. Press enter to return to main menu. \n\n >>> ")
        main()
        
def info(): 
    os.system("clear")
    print(banner)
    print("""
╔═════════════════════════════════════════════════════════════════╗
║                            - Info -                             ║
╠═════════════════════════════════════════════════════════════════╣
║ ╔════════════════╦════════════════════════════════════════════╗ ║
║ ║ Full Name      ║ Search by full name (e.g., John Doe)       ║ ║
║ ╠════════════════╬════════════════════════════════════════════╣ ║
║ ║ Username/ALias ║ Search by username (e.g., johndoe)         ║ ║
║ ╠════════════════╬════════════════════════════════════════════╣ ║
║ ║ Phone Number   ║ Search by phone number                     ║ ║
║ ║                ║ (e.g., +15551234567)                       ║ ║
║ ╠════════════════╬════════════════════════════════════════════╣ ║
║ ║ Email Address  ║ Search by email address                    ║ ║
║ ║                ║ (e.g., john.doe@example.com)               ║ ║
║ ╠════════════════╬════════════════════════════════════════════╣ ║
║ ║ IP Address     ║ Search by IP address (e.g., 192.168.1.1)   ║ ║
║ ╠════════════════╬════════════════════════════════════════════╣ ║
║ ║ Domain Name    ║ Search by domain name (e.g., example.com)  ║ ║
║ ╠════════════════╬════════════════════════════════════════════╣ ║
║ ║ Document URL   ║ Search by Google Document URL              ║ ║
║ ║                ║ (e.g., docs.google.com/document/d/...)     ║ ║
║ ╠════════════════╬════════════════════════════════════════════╣ ║
║ ║ Discord ID     ║ Search by Discord username#tag or user ID  ║ ║
║ ║                ║ (e.g., johndoe#1234 or 123456789012345678) ║ ║
║ ╠════════════════╬════════════════════════════════════════════╣ ║
║ ║ Minecraft      ║ Search by Minecraft username (e.g., Notch) ║ ║
║ ╚════════════════╩════════════════════════════════════════════╝ ║
╠═════════════════════════════════════════════════════════════════╣
║                       Enter to go Back                          ║
╚═════════════════════════════════════════════════════════════════╝
  
""")
    input(" >>> ") 
    search()

def main():
    os.system("clear")
    print(banner)
    print(menu)
    menu_choice = input(" >>> ").strip().lower()
    if menu_choice == "1":
        search()
    elif menu_choice == "2":
        update_token()
    elif menu_choice == "3":
        update_tool()
    elif menu_choice == "x":
        os.system("clear")
        sys.exit()
    else:
        input(Fore.RED + "\nInvalid Input. Try Again. " + Style.RESET_ALL)
        os.system("clear")
        main()

def search():
    os.system("clear")
    print(banner)
    global api_key
    if api_key is None:
        api_key = get_api_key()
        if api_key is None:
            print("\nAPI key is required for searching.")
            key_err = input("\nAdd Key to file now? (y/n): ").strip().lower()
            if key_err == "y":
                update_token()
            else:
                main()
    plugin_type_choice = input("""
    ╔═══════════════════════════════════════════════╗
    ║                   - Search -                  ║
    ╠═══════════════════════════════════════════════╣
    ║ ╔════════════════════╗ ╔════════════════════╗ ║
    ║ ║ [1] Full Name      ║ ║ [6] Domain Name    ║ ║
    ║ ║ [2] Username/ALias ║ ║ [7] Document URL   ║ ║
    ║ ║ [3] Phone Number   ║ ║ [8] Discord ID     ║ ║
    ║ ║ [4] Email Address  ║ ║ [9] Minecraft      ║ ║
    ║ ║ [5] IP Address     ║ ║                    ║ ║
    ║ ╚════════════════════╝ ╚════════════════════╝ ║
    ╠═══════════════╦═══════════════╦═══════════════╣
    ║   [b] Back    ║   [i] Info    ║   [x] Exit    ║
    ╚═══════════════╩═══════════════╩═══════════════╝

 >>> """).strip().lower()

    plugin_type = {
    "1": "fullname",
    "2": "username",
    "3": "phone",
    "4": "email",
    "5": "ip",
    "6": "domain",
    "7": "document",
    "8": "discord",
    "9": "minecraft",
}

    if plugin_type_choice in plugin_type:
        plugin_type_value = plugin_type[plugin_type_choice]
    elif plugin_type_choice == "b":
        main()
    elif plugin_type_choice == "x":
        os.system("clear")
        sys.exit()
    elif plugin_type_choice == "i":
        os.system("clear")
        info()
    else:
        input(Fore.RED + "\nInvalid Input. Try Again. " + Style.RESET_ALL)
        os.system("clear")
        search()

    plugin_name_map = {
    "fullname": "First and Last Name",
    "username": "Username",
    "phone": "Phone Number",
    "email": "Email Address",
    "ip": "IP Address",
    "domain": "Domain",
    "document": "Document URL",
    "discord": "Discord ID",
    "minecraft": "Minecraft ID",
}
    if plugin_type_value in plugin_name_map:
        plugin_print = plugin_name_map[plugin_type_value]
    else:
        input(Fore.RED + "\nError. " + Style.RESET_ALL)
        os.system("clear")
        search()

    os.system("clear")
    print(banner)
    target_value = input(f"\n\n{plugin_print} to search:  ")
    search_id_value = input("\nCustom search ID. Leave blank to auto generate: ")
    report_choice = input("\nInclude final summary report (y/n): ").strip().lower()
    if report_choice == "y":
        report_value = "True"
    elif report_choice == "n":
        report_value = "False"
    else:
        report_value = "True"

    params = {
        "target": target_value,
        "plugin_type": plugin_type_value,
        "searchId": search_id_value,
        "report": report_value,
        "_": int(time.time() * 1000)
    }
    headers = {
        "Authorization": f"Bearer {'*' * 8}"
    }

    full_response_data = []

    try:
        print(f"\nSending GET request to: {base_url}")
        print(f"Using parameters: {params}")
        print(f"Using headers: {headers}")
        headers["Authorization"] = f"Bearer {api_key}"
        response = requests.get(base_url, params=params, headers=headers, stream=True)

        if response.status_code == 200:
            print("\nRequest successful! Streaming response: \n")
            try:
                for line in response.iter_lines():
                    if line:
                        decoded_line = line.decode('utf-8')
                        if decoded_line.startswith('data:'):
                            json_data = decoded_line[5:].strip()
                            try:
                                data = json.loads(json_data)
                                full_response_data.append(data)
                                print(json.dumps(data, indent=2))
                                if data.get("status") == "stream_closed":
                                    break
                            except json.JSONDecodeError:
                                print(f"Could not decode JSON from line: {json_data}")
                        else:
                             print(f"Received non-data line: {decoded_line}")
            except requests.exceptions.RequestException as e:
                 print(f"Error during streaming: {e}")
        else:
            print(f"\nRequest failed with status code: {response.status_code}")
            print("Response content:")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"\nAn error occurred: {e}")

    save_choice = input("\nWould you like to save the response? (y/n): ").strip().lower()
    if save_choice == "y":
        file_name = input("Enter file name to save (without extension): ").strip()
        if not file_name:
             print(Fore.RED + "File name cannot be empty." + Style.RESET_ALL)
        else:
            save_directory = os.path.join(os.path.expanduser("~"), "nosint", "saved")
            os.makedirs(save_directory, exist_ok=True)
            file_path = os.path.join(save_directory, f"{file_name}.json")
            try:
                with open(file_path, "w") as f:
                    json.dump(full_response_data, f, indent=2)
                print(Fore.GREEN + f"Response saved to {file_path}" + Style.RESET_ALL)
            except IOError:
                print(Fore.RED + f"Error saving file to {file_path}" + Style.RED)

    input("\nPress Enter to return to search menu.")
    search()

init()
api_key = get_api_key()
main()
