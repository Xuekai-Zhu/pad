def solution():
    """Emily can type 60 words per minute. How many hours does it take her to write 10,800 words?"""
    # Define Emily's typing speed
    SPEED = 60  # words per minute

    # Define the number of words to be typed
    WORDS = 10800

    # Calculate the time taken to type the given number of words
    time_in_minutes = WORDS / SPEED
    time_in_hours = time_in_minutes / 60

    # Display the time taken in hours
    result = time_in_hours
    return result

print(solution())