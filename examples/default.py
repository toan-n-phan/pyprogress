import time
import random

import pyprogress as pb

def main():
    bar = pb.ProgressBar()
    for i in range(95):
        bar.increase(1)
        random_secs = (random.random()) / 10
        time.sleep(random_secs)
    bar.set_progress(100)

if __name__ == "__main__":
    main()
    