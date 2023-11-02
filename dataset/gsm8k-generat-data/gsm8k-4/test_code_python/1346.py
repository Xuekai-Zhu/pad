def solution():
    """The central Texas countryside contains many toads that come out at night.  For every green toad, there are 25 brown toads, and one-quarter of the brown toads are spotted.  If there are 50 spotted brown toads per acre, how many green toads are there per acre?"""
    # Calculate the number of brown toads per acre
    brown_toads_total = 50 / 0.25

    # Calculate the total number of toads (brown + green) per acre
    total_toads = brown_toads_total + 1

    # Calculate the number of green toads per acre
    green_toads = total_toads / 26

    result = green_toads
    return result

print(solution())