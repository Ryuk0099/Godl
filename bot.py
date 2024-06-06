import subprocess
import time

def restart_bot():
    while True:
        try:
            # Replace 'your_bot_script.py' with the path to your bot script
            process = subprocess.Popen(['python3', 'm.py'])
            process.wait()
        except Exception as e:
            print(f'Bot crashed with error: {e}. Restarting...')
        time.sleep(5)  # Wait for 5 seconds before restarting

if name == "main":
    restart_bot()
