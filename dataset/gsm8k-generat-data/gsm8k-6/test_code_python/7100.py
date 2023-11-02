def solution():
    # Calculate the number of words Gunther can type in a day
    words_per_minute = 160/3  # words Gunther can type in a minute
    total_words = words_per_minute * 480  # total words Gunther can type in a day
    result = total_words
    return result

print(solution())