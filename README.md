### SpsBrute-force

[![GitHub stars](https://img.shields.io/github/stars/RKgroupkg/SpsBrute-force?style=social)](https://github.com/RKgroupkg/SpsBrute-force)
[![Forks](https://img.shields.io/github/forks/RKgroupkg/SpsBrute-force?style=social)](https://github.com/RKgroupkg/SpsBrute-force/forks)
[![License](https://img.shields.io/github/license/RKgroupkg/SpsBrute-force?style=flat)](https://github.com/RKgroupkg/SpsBrute-force/blob/main/LICENSE)

Welcome to **SpsBrute-force**, a powerful brute force tool designed for testing login credentials on the SPS Purnea ERP system.

![SpsBrute-force Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5f4E3rl9YbpO17er1dZGsCBygDt9x6TPgPw&usqp=CAU) <!-- Replace with your logo or a relevant image -->

### Penetration Testing Tool

Welcome to the **SpsBrute-force** repository! This tool is designed to assist in testing the security of your website by simulating various attack scenarios. Please ensure you have explicit permission before using this tool on any website.

## Features

- **Automated Credential Testing**: Efficiently test multiple username and password combinations.
- **Parallel Processing**: Leverage asynchronous operations for faster execution.
- **Detailed Reporting**: Receive comprehensive logs and reports of the testing process.

## Installation :-

# 1. Git and Python Installation Guide

This guide provides step-by-step instructions for installing Git and Python on both Windows and Termux (Android).

# Windows Installation

 Installing Git on Windows

1. Download Git:
   - Visit [Git for Windows](https://git-scm.com/download/windows)
   - The download should start automatically

2. Install Git:
   - Run the downloaded `.exe` file
   - Click "Next" and accept the license
   - Choose installation location (default is recommended)
   - Select components (default options are fine for most users)
   - Choose default editor (Notepad is recommended for beginners)
   - Click "Install"
   - Click "Finish" when done

3. Verify installation:
   - Open Command Prompt (cmd)
   - Type: `git --version`
   - You should see the Git version number

# Installing Python on Windows

1. Download Python:
   - Visit [Python Downloads](https://www.python.org/downloads/)
   - Click "Download Python" (latest version)

2. Install Python:
   - Run the downloaded `.exe` file
   - **Important:** Check "Add Python to PATH"
   - Click "Install Now"
   - Wait for installation to complete
   - Click "Close" when finished

3. Verify installation:
   - Open Command Prompt (cmd)
   - Type: `python --version`
   - Type: `pip --version`
   - Both commands should show version numbers

## Termux Installation (Android)
# Installing Termux (Android)

○ Method 1: F-Droid (Recommended)
1. Visit [F-Droid's website](https://f-droid.org)
2. Download and install F-Droid app
3. Open F-Droid and search for "Termux"
4. Install Termux from F-Droid

○ Method 2: Google Play Store (Not Recommended)
âš ï¸ **Note:** The Play Store version is no longer maintained. Use F-Droid version for latest updates.

# Installing Git on Termux

1. Update package list:
   ```bash
   pkg update && pkg upgrade
   ```

2. Install Git:
   ```bash
   pkg install git
   ```

3. Verify installation:
   ```bash
   git --version
   ```

# Installing Python on Termux

1. Install Python:
   ```bash
   pkg install python
   ```

2. Verify installation:
   ```bash
   python --version
   pip --version
   ```


## Troubleshooting

# Windows
- If `git` or `python` commands aren't recognized, restart your computer
- Make sure "Add to PATH" was selected during Python installation
- Try running Command Prompt as Administrator

# Termux
- If packages fail to install, run `pkg update && pkg upgrade`
- If permission denied, add `termux-setup-storage`
- Try closing and reopening Termux

# Need Help?
- Git Documentation: [https://git-scm.com/doc](https://git-scm.com/doc)
- Python Documentation: [https://docs.python.org](https://docs.python.org)
- Termux Wiki: [https://wiki.termux.com](https://wiki.termux.com)

## 2. **Cloneing the Repository**:

   ```bash
   git clone https://github.com/RKgroupkg/SpsBrute-force.git
   cd SpsBrute-force
   ```
## 3. How to Run the Script

After cloning the repository, follow these steps to run the `SpsBrute.py` script:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have cloned the repository using the `cd` command:
   ```bash
   cd SpsBrute-force
   ```
   1. Once you're inside the directory, run the script by typing:
     ```bash
     python SpsBrute.py
     ```

   2. now install all the requirements
      ```bash
      pip install aiohttp beautifulsoup4 tqdm colorama
      ```

   3. For help on how to input value use
    ```bash
     python SpsBrute.py -h
    ```

    
### Disclaimer
Please note: This script is intended for educational and ethical testing purposes only. Use it responsibly, and do not attempt unauthorized access to any systems. The author and the repository are not responsible for any misuse or damages caused by running this script


#### Contact
[![Telegram](https://img.shields.io/badge/Join%20Telegram-%40Rkgroup5316-0088cc?style=for-the-badge&logo=telegram)](https://t.me/Rkgroup5316)

[![BuyMeACoffee](https://img.shields.io/badge/Support%20me%20on-Buy%20Me%20a%20Coffee-FF813F?style=for-the-badge&logo=buymeacoffee)](https://buymeacoffee.com/Rkgroup)


<p align="center">
  <a href="https://t.me/Rkgroup_Bot">
    <img src="https://img.shields.io/static/v1?label=Join&message=Telegram%20Channel&color=blueviolet&style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Channel" />
  </a>
  <a href="https://telegram.me/Rkgroup_helpbot">
    <img src="https://img.shields.io/static/v1?label=Join&message=Telegram%20Group&color=blueviolet&style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Group" />
  </a>
</p>
