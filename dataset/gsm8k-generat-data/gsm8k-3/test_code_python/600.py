def solution():
    """Mike can type 65 words per minute. Due to a minor accident, Mike cannot use his right hand for a while so that his typing speed is now 20 words less per minute. If he is supposed to type a document with 810 words, how many minutes will it take him to finish typing the document?"""
    # Calculate Mike's new typing speed
    new_speed = 65 - 20

    # Calculate the time it will take him to type the document with the new speed
    time = 810 / new_speed

    # Display the time in minutes
    result = time
    return result

print(solution())