from typing import TextIO

def overwrite(stdout: TextIO, text: str) -> None:
    """Overwrite the current line by moving the cursor to the front.
    """
    stdout.write('\r')
    stdout.write(text)
    stdout.flush()
