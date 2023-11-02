def solution():
    """Emily can type 60 words per minute. How many hours does it take her to write 10,800 words?"""
    # Define the typing speed and the number of words to type
    typing_speed = 60
    words_to_type = 10800

    # Calculate the time it takes to type the given number of words at the given speed
    minutes = words_to_type / typing_speed
    hours = minutes / 60

    # return the result
    result = hours
    return result

print(solution())