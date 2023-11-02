def solution():
    """Abigail has a report due tomorrow which needs to be 1000 words in length. Abigail can type 300 words in half an hour. If she has already written 200 words, how many more minutes will it take her to finish the report?"""
    # Calculate the remaining words to be typed
    remaining_words = 1000 - 200

    # Calculate the time needed to type the remaining words
    time_needed = (remaining_words / 300) * 30

    # Display the time needed in minutes
    result = time_needed
    return result

print(solution())