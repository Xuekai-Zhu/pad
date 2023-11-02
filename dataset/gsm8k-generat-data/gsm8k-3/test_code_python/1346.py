def solution():
    """The central Texas countryside contains many toads that come out at night.  For every green toad, there are 25 brown toads, and one-quarter of the brown toads are spotted.  If there are 50 spotted brown toads per acre, how many green toads are there per acre?"""
    # Calculate the number of brown toads (spotted and non-spotted) per acre
    brown_toads = 50 * 4

    # Calculate the total number of toads (green and brown) per acre
    total_toads = brown_toads * 26

    # Calculate the number of green toads per acre
    green_toads = total_toads / 26

    # Display the number of green toads per acre
    result = green_toads
    return result

print(solution())