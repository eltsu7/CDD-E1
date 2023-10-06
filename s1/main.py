from datetime import datetime
import time
import pathlib
import requests
import os


def main():
    log_path = pathlib.Path("/tmp/logs/client.log")
    print(os.getcwd())
    log_path.parent.mkdir(exist_ok=True)
    log_file = open(log_path, "w")  # "w" creates and removes everything in the file

    for i in range(1, 21):
        url = os.getenv("service2url")
        url = "http://server:8000"
        text = f"{i} {datetime.now()} {url}"
        log_file.write(text + "\n")

        print(f"Sending: {text}")
        requests.post(
            url=url,
            data=text
        )
        time.sleep(2)

    # Leave container running, used for debug
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()