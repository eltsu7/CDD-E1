from datetime import datetime
import time
import pathlib
import requests
import os


def main():
    log_path = pathlib.Path("/tmp/logs/service1.log")
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


if __name__ == "__main__":
    main()