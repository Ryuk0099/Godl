def restart_bot():
    while True:
        try:
            # Replace 'your_bot_script.py' with the path to your bot script
            subprocess.run(['python3', 'm.py'], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Bot crashed with error: {e}. Restarting...')
            time.sleep(5)  # Wait for 5 seconds before restarting

if name == "main":
    restart_bot()
