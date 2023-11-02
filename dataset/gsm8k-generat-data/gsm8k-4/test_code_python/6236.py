def solution():
    """Abigail has a report due tomorrow which needs to be 1000 words in length. Abigail can type 300 words in half an hour. If she has already written 200 words, how many more minutes will it take her to finish the report?"""
    # Define the total number of words needed in the report
    total_words = 1000

    # Define the typing speed in words per minute
    typing_speed = 10

    # Calculate the remaining number of words to be typed
    remaining_words = total_words - 200

    # Calculate the time needed to finish typing the report in minutes
    time_needed = remaining_words / typing_speed

    # Return the result
    result = time_needed * 60
    return result

print(solution())