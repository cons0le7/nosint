# 👁️‍🗨️ NoSINT 
API wrapper for [NoSINT](https://nosint.org). Works on Arch, Debian, Android with Termux and iOS with iSH Shell.

![Image](https://github.com/user-attachments/assets/86ba8d86-d079-47ba-a7d9-fdd64b0a0c8c)

## ⚠️ Before Installing ⚠️
You will first need to [register](https://nosint.org/auth/register) at nosint.org to acquire your API token.

## 🛠️ Install 🛠️

### [![Arch Linux](https://img.shields.io/badge/Arch%20Linux-%230C8BDC?style=for-the-badge&logo=arch-linux&logoColor=white)](#)
- Install dependencies: 
```
sudo pacman -Syu git python python-pip
```
- Install tool: 
```
cd ~
git clone https://github.com/cons0le7/nosint.git
chmod +x ~/nosint/nosint ~/nosint/update/update.sh ~/nosint/update/update_2.sh
sudo ln -s ~/nosint/nosint /usr/bin/nosint
sudo nosint
```

### [![Debian](https://img.shields.io/badge/Debian-A81D33?style=for-the-badge&logo=debian&logoColor=fff)](#)
- Install dependencies: 
```
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install git python3 python3-pip
```
- Install tool: 
```
cd ~
git clone https://github.com/cons0le7/nosint.git
chmod +x ~/nosint/nosint ~/nosint/update/update.sh ~/nosint/update/update_2.sh
sudo ln -s ~/nosint/nosint /usr/local/bin/nosint
sudo nosint
```

### [![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)](#)
In Termux: 
- Install dependencies: 
```
apt-get update && apt-get upgrade -y
apt-get install git python python-pip
```
- Install tool: 
```
cd $HOME
git clone https://github.com/cons0le7/nosint.git
chmod +x $HOME/nosint/nosint $HOME/nosint/update/update.sh $HOME/nosint/update/update_2.sh 
ln -s $HOME/nosint/nosint /data/data/com.termux/files/usr/bin/nosint
nosint
```
### [![iOS](https://img.shields.io/badge/iOS-000000?style=for-the-badge&logo=apple&logoColor=white)](#)
In iSH Shell: 
- Install dependencies: 
```
apk add git bash python3 py3-pip 
```
- Install tool: 
```
cd $HOME
git clone https://github.com/cons0le7/nosint.git
chmod +x $HOME/nosint/nosint $HOME/nosint/update/update.sh $HOME/nosint/update/update_2.sh 
ln -s $HOME/nosint/nosint /usr/bin/nosint
nosint
```
## Usage: 
- Call `nosint` in terminal to execute if you are on Termux, iSH Shell or if you are root. Use `sudo nosint` otherwise. 
- When running script for the first time you will be prompted to enter API key. After entering key, you will be asked if you want to save key to file or not.
- If you choose to save token it will be stored in `~/.nosint/api.key`

### Main menu: 
- [Search](https://github.com/cons0le7/nosint?tab=readme-ov-file#search-menu)
- [Update Token](https://github.com/cons0le7/nosint?tab=readme-ov-file#update-token)
- [Update Tool](https://github.com/cons0le7/nosint?tab=readme-ov-file#update-tool)
- [View Saved](https://github.com/cons0le7/nosint?tab=readme-ov-file#view-saved)
- Exit

#### Search menu:  
Options: 
- Full Name - Search by full name (e.g., John Doe)
- Username/Alias - Search by username (e.g., johndoe)
- Phone Number - Search by phone number (e.g., +15551234567)
- Email Address - Search by email address (e.g., john.doe@example.com)
- IP Address - Search by IP address (e.g., 192.168.1.1)
- Domain Name - Search by domain name (e.g., example.com)
- Document URL - Search by Google Document URL (e.g., docs.google.com/document/d/...)
- Discord - Search by Discord username#tag or user ID (e.g., johndoe#1234 or 123456789012345678)
- Minecraft - Search by Minecraft username (e.g., Notch)

Info on each option is is accessible by typing `i` within this menu.

#### Search process: 
- After selecting search option you will be prompted to enter your query.  
- The following prompt will ask for a custom search ID which you can use for your own tracking / record keeping. You can leave this blank to have it auto-generate.
- Final summary report defaults to yes if no choice is selected. Search begins after entering.

####  Responses: 
The API will stream a series of 5 responses back to you: 
- connecting
- plugins_discovered
- search_started
- batch_results
- completed

After completion, you have the option to save the response. If you choose yes, you will then be prompted to enter file name. Saved responses are stored in `~/.nosint/saved` as JSON. 

#### Update Token: 
- Gives the option to change  authentication token stored in api.key

#### Update Tool: 
- Fetches latest version of tool from GitHub
- Will completely overwrite tool directoy. Stored token and saved data will not be affected as they are located outside of the tool directory.

#### View Saved: 
- Lists files in `~/.nosint/saved`
- Type file name without extension to view using `less` or press **Enter** to return to main menu.

After file is opened: 
- Use **space** for next page `b` for previous page.
- Type `g` to move to top line, `G` to move to bottom line.
- **Enter** for next line, `k` for previous line (or you can use **up arrow** and **down arrow** keys).
- Use `/` + query + **Enter** to search forwards.
- Use `?` + query + **Enter** to search backwards.
- Type `N` to find next occurrence or `n` to find previous occurrence of query.
- Type `q` to quit the viewing session and return to the script. 


## 🗑️ Uninstall 🗑️
```
cd $HOME/nosint
chmod +x uninstall.sh
./uninstall.sh
```
Executing uninstall.sh will prompt for confirmation. If you choose to uninstall, the script will: 
- Delete the tool directory at `~/nosint`
- Remove the symbolic link from whichever path it is in (`/usr/bin/nosint`, `/data/data/com.termux/files/usr/bin/nosint` or `/usr/local/bin/nosint`) depending on your OS.
- Delete `api.key` in `~/.nosint`
- Give the option to either retain your saved data in `~/.nosint/saved` or not. If you choose to delete saved data the entire `~/.nosint` directory will be deleted.


><br>## ⚠️ Disclaimer ⚠️</br>

This tool intended to be used legally and ethically. I do not promote or condone any illegal or criminal activity. I am not responsible for any use or misuse of this tool. 
