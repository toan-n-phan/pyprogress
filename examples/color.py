import time
import random

import pyprogress as pb

def main():
    green_square = '\u001b[32m█\u001b[0m'
    theme = pb.Theme(green_square)
    bar = pb.ProgressBar(theme=theme)
    for i in range(90):
        bar.increase(1)
        random_secs = (random.random()) / 10
        time.sleep(random_secs)
    bar.set_progress(100)

if __name__ == "__main__":
    main()
    