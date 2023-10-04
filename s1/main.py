from datetime import datetime
import time
import os
import pathlib


def main():
    log_path = pathlib.Path(".\\logs\\service1.log")
    log_path.parent.mkdir(exist_ok=True)
    log_file = open(log_path, "w")  # "w" creates and removes everything in the file

    for i in range(1, 21):
        text = f"{i} {datetime.now()}"
        log_file.write(text + "\n")
        send_http_message(text)
        time.sleep(0.1)

def send_http_message(message: str):
    print(f"Sending: {message}")

if __name__ == "__main__":
    main()