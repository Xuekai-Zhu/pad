def solution():
    micah_typing_rate = 20  # words per minute
    isaiah_typing_rate = 40  # words per minute
    minutes_per_hour = 60  # minutes

    # Calculate the number of words typed by Micah and Isaiah in an hour
    micah_words_per_hour = micah_typing_rate * minutes_per_hour
    isaiah_words_per_hour = isaiah_typing_rate * minutes_per_hour

    # Calculate the difference in the number of words typed by Micah and Isaiah in an hour
    difference = isaiah_words_per_hour - micah_words_per_hour
    result = difference
    return result

print(solution())