def solution():
    """Several birds were sitting in the branches of a crape myrtle tree.  There were three times more cardinals than bluebirds, but half as many swallows as bluebirds. If there were 2 swallows, what is the total number of birds in the crape myrtle tree?"""
    # Define the number of swallows and the ratio of cardinals to bluebirds
    swallows = 2
    cardinals_ratio = 3

    # Calculate the number of bluebirds
    bluebirds = swallows * 2 # half as many swallows as bluebirds

    # Calculate the number of cardinals
    cardinals = bluebirds * cardinals_ratio

    # Calculate the total number of birds
    total_birds = swallows + bluebirds + cardinals

    # Display the total number of birds
    result = total_birds
    return result

print(solution())