import datetime

def log_message(contact, message):
    with open("message_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}"
                       f"- Sent to {contact['name']}: {message}\n")

def display_logs():
    """Displays the logs from the log file."""
    try:
        with open(log_file, "r") as log_file:
            for line in log_file:
                print(line.strip())
    except FileNotFoundError:
        print("No logs available yet.")