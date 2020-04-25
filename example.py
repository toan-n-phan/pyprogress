import time
import random

import pyprogress.progressbar as pb

def main():
    bar = pb.ProgressBar()
    for i in range(90):
        bar.increase(1)
        random_secs = (random.random()) / 10
        time.sleep(random_secs)

if __name__ == "__main__":
    main()
    