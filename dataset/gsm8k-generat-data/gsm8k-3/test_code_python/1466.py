def solution():
    """A dog barks 30 times per minute. If 2 dogs bark 30 times per minute, how many times will they have barked after 10 minutes?"""
    # Define the number of barks per minute per dog
    BARKS_PER_MINUTE_PER_DOG = 30

    # Define the number of dogs
    NUM_DOGS = 2

    # Define the number of minutes
    NUM_MINUTES = 10

    # Calculate the total number of barks
    total_barks = BARKS_PER_MINUTE_PER_DOG * NUM_DOGS * NUM_MINUTES

    # Display the total number of barks
    result = total_barks
    return result

print(solution())