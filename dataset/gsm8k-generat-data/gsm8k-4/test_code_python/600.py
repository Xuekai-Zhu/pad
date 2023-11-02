def solution():
    """Mike can type 65 words per minute. Due to a minor accident, Mike cannot use his right hand for a while so that his typing speed is now 20 words less per minute. If he is supposed to type a document with 810 words, how many minutes will it take him to finish typing the document?"""
    # Define the original typing speed and the amount decreased by the accident
    original_speed = 65
    decrease_speed = 20

    # Calculate the new typing speed after the accident
    new_speed = original_speed - decrease_speed

    # Define the total number of words to type
    total_words = 810

    # Calculate the total time to finish typing the document
    time = total_words / new_speed

    # Return the result
    result = time
    return result

print(solution())