def solution():
    # Calculate the number of words Micah can type in one hour
    micah_words_per_hour = 20 * 60

    # Calculate the number of words Isaiah can type in one hour
    isaiah_words_per_hour = 40 * 60

    # Calculate the difference between the number of words Isaiah and Micah can type in one hour
    words_difference = isaiah_words_per_hour - micah_words_per_hour
    result = words_difference
    return result

print(solution())