def solution():
    # Calculate the number of words Gunther can type in one minute
    words_per_minute = 160 / 3

    # Calculate the total number of words Gunther can type in one day
    words_per_day = words_per_minute * 60 * 8  # Gunther works for 8 hours, or 480 minutes

    result = words_per_day
    return result

print(solution())