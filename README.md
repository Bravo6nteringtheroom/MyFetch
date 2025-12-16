MYFetch 🚀

MYFetch is a lightweight, Python-based system information tool, inspired by Neofetch, that displays your OS, hardware, and resource usage alongside an awesome ASCII logo — all in your terminal!

🌟 Features

Displays OS name and version

Shows hostname and IP address

Shows CPU type, cores, and usage

Shows RAM usage

Shows disk usage

Shows system uptime

Custom ASCII logos that can be switched dynamically

Colorful output with ANSI and hex colors for style

Easy to extend with more system info

🎨 Logos

MYFetch supports multiple ASCII logos! You can switch between them easily:

logo1 — Classic design

logo2 — Neon-inspired

logo3 — Minimalist

Just update the logo_lines variable or create your own.

🖥 Installation

Clone the repository:

git clone https://github.com/<yourusername>/MYFetch.git
cd MYFetch


Install dependencies:

pip install psutil screeninfo GPUtil


(Optional: GPUtil only if you want GPU info.)

⚡ Usage
python main.py


Example output:

    (  ___  )     OS: Linux-6.12
    | (   ) |     CPU Type: Intel i7
    | |   | |     CPU Usage: 12%
    | |   | |     CPU Cores: 8
    | |   | |     RAM Used: 8 / 16 GB
    | (___) |
    (_______)

🔧 Customization

Change logo: Edit or replace logo_lines in the code

Add system info: Add more fields to info_lines

Colors: Use ANSI codes or hex colors for each field

Dynamic logos: Swap logos at runtime
