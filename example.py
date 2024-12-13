import argparse
import datetime
from dotenv import load_dotenv
import time
from tqdm import trange
from sophy import Slackbot

load_dotenv()

def pst_time():
    return datetime.datetime.now(datetime.timezone.utc).astimezone(datetime.timezone(datetime.timedelta(hours=-8))).strftime("%Y-%m-%d %H:%M:%S")

def main(args):
    bot = Slackbot(args.email)
    bot.notify("{}: Starting training...".format(pst_time()))

    epochs = 10
    for i in trange(epochs, desc='Training'):
        # Tell the program to sleep for 10 seconds
        time.sleep(0.5)
        bot.notify("{}: Finished epoch {}".format(pst_time(), i))
    
    bot.notify("{}: Training complete!".format(pst_time()))

    print("Done!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', type=str, required=True)
    args = parser.parse_args()
    
    main(args)