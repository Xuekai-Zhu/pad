def solution():
    """Barbara Blackburn can type 212 words per minute. Due to Carpal tunnel syndrome, Barbara cannot use her left hand for a while so her typing speed is now 40 words less per minute. If she is supposed to type a document with 3440 words, how many minutes will it take her to finish typing the document?"""
    # Define the original typing speed and decrease due to Carpal tunnel syndrome
    original_speed = 212
    decreased_speed = original_speed - 40

    # Define the number of words to be typed
    words_to_type = 3440

    # Calculate the time it takes to type with the original speed and the decreased speed
    original_time = words_to_type / original_speed
    decreased_time = words_to_type / decreased_speed

    # Choose the time it takes with the slower speed
    time = decreased_time

    result = round(time)
    return result

print(solution())