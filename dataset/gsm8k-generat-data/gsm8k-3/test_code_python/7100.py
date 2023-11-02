def solution():
    """Gunther can type 160 words every 3 minutes and he works 480 minutes per day. How many words can Gunther type in a working day?"""
    # Calculate how many 3-minute intervals Gunther works in a day
    intervals_per_day = 480 // 3

    # Calculate how many words Gunther types in one 3-minute interval
    words_per_interval = 160

    # Multiply the number of intervals by the number of words per interval to find the total number of words typed
    total_words = intervals_per_day * words_per_interval

    # Display the total number of words typed
    result = total_words
    return result

print(solution())