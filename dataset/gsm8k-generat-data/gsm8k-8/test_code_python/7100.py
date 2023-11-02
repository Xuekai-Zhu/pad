def solution():
    # Calculate how many sets of 3 minutes Gunther works in a day
    sets_of_3_min = 480 / 3

    # Calculate how many words Gunther types in one set of 3 minutes
    words_per_set = 160

    # Calculate the total number of words Gunther types in a day
    total_words = sets_of_3_min * words_per_set
    result = total_words
    return result

print(solution())