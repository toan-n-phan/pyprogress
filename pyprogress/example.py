import time
import random

import progressbar as pb

def main():
    bar = pb.ProgressBar()
    for i in range(90):
        bar.increase(1)
        random_secs = (random.random()) / 10
        time.sleep(random_secs)
    
    # print("zxcdadsda das dasd a", end="\r")
    # time.sleep(1)
    # print("asddadsda das dasd a", end="\r")
    # time.sleep(1)
    # print("qwedadsda das dasd a", end="\r")
    # time.sleep(1)
    # print()

if __name__ == "__main__":
    main()
    