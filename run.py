from highrise import BaseBot
from asyncio import run as arun
import time

# Import your Bot class from main.py
from main import Bot

class RunBot:
    room_id = "66d2726b2e80dd1f614c4dbb"  # Room ID
    bot_token = "432f23df3fc5076fe6c95ade994a533c9d473ecdb56acc31346899a94d6aaa6d"  # Bot token

    def run_loop(self) -> None:
        while True:
            try:
                # Create an instance of the Bot and start it
                arun(Bot().start(self.room_id, self.bot_token))
            except Exception as e:
                print("Error: ", e)
                time.sleep(5)

if __name__ == "__main__":
    RunBot().run_loop()
