import time
import math

def progress_bar(current, total, elapsed_time, char_to_use="#"):
    """
    Return a string that details the current progress using hashtags.
    
    # ARGUMENTS
    current         -> The current progress.
    total           -> The total of the progress.
    elapsed_time    -> How much time has passed, in seconds
    char_to_use     -> What character to use to represent a "filled" progress bar
    """
    max_hashtag = 30
    num_hashtags = math.floor(current / total * max_hashtag)
    s = ""
    for i in range(num_hashtags):
        s = "".join((s, char_to_use))
    for i in range(max_hashtag - num_hashtags):
        s = "".join((s, " "))
    
    return_string = "[{}] {:.2%}, {:.2f} seconds collapsed".format(s, current / total, elapsed_time)
    return return_string


def test(total):
    start_time = time.time()
    for x in range(total):
        end_time = time.time()
        elapsed_time = end_time - start_time
        s = progress_bar(x + 1, total, elapsed_time, char_to_use="=")
        print(s, end="\r")
    print("")


def print_progress_bar():
    start_time = time.time()
    total = 234023;
    for x in range(10):
        elapsed_time = time.time() - start_time
        print('\r{:d}/{:d}, {:.2%}, {:.2f} seconds elapsed'.format(x, total, x/total, elapsed_time), end="")
        time.sleep(0.5)
    print()


def get_num_hashtags(num_hashtags, max_hashtags):
    s = ""
    for i in range(num_hashtags):
        s = "".join((s, "#"))
    for i in range(max_hashtags - num_hashtags):
        s = "".join((s, " "))

    return s


def progress_bar_test(total):
    max_hashtag = 20
    counter = 0
    starttime = time.time()
    for x in range(total):
        endtime = time.time()
        elapsedtime = endtime - starttime
        percent_done = math.floor((x + 1) / total * max_hashtag)
        num_hashtags = get_num_hashtags(percent_done, max_hashtag)
        print("[{}] {:.2%}, {:.2f} seconds elapsed".format(num_hashtags, x / total, elapsedtime), end="\r")
    print("")


if __name__ == "__main__":
    total = 32767
    test(total)
