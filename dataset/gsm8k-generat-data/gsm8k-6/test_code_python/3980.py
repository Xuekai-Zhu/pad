def solution():
    swallows = 2  # given number of swallows
    bluebirds = swallows * 2  # there are half as many swallows as bluebirds
    cardinals = bluebirds * 3  # there are three times more cardinals than bluebirds

    # Calculate the total number of birds in the tree
    total_birds = swallows + bluebirds + cardinals
    result = total_birds
    return result

print(solution())