def solution():
    """Barbara Blackburn can type 212 words per minute. Due to Carpal tunnel syndrome, Barbara cannot use her left hand for a while so her typing speed is now 40 words less per minute. If she is supposed to type a document with 3440 words, how many minutes will it take her to finish typing the document?"""
    # Define Barbara's typing speed with her current condition
    current_speed = 212 - 40

    # Define the number of words in the document
    num_words = 3440

    # Calculate the time it will take Barbara to finish typing the document
    time_minutes = num_words / current_speed

    # Convert the time to minutes rounded up to the nearest minute
    time_minutes = math.ceil(time_minutes)

    # Display the time it will take Barbara to finish typing the document
    result = time_minutes
    return result

print(solution())