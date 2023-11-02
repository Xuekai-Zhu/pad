def solution():
    """Micah can type 20 words per minute and Isaiah can type 40 words per minute. How many more words can Isaiah type than Micah in an hour?"""
    # Define the word per minute for Micah and Isaiah
    micah_wpm = 20
    isaiah_wpm = 40

    # Calculate the number of words Micah and Isaiah can type in an hour
    micah_words_per_hour = micah_wpm * 60
    isaiah_words_per_hour = isaiah_wpm * 60

    # Calculate the difference in words per hour between Micah and Isaiah
    difference = isaiah_words_per_hour - micah_words_per_hour

    result = difference
    return result

print(solution())