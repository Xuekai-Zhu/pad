def solution():
    """Bart makes a mixtape.  The first side has 6 songs.  The second side has 4 songs.  Each song is 4 minutes.  How long is the total tape?"""
    # Calculate the total length of the first side
    side1 = 6 * 4 # each song is 4 minutes long

    # Calculate the total length of the second side
    side2 = 4 * 4 # each song is 4 minutes long

    # Calculate the total length of the mixtape
    total_length = side1 + side2

    # Display the total length of the mixtape
    result = total_length
    return result

print(solution())