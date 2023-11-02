def solution():
    """Several birds were sitting in the branches of a crape myrtle tree. There were three times more cardinals than bluebirds, but half as many swallows as bluebirds. If there were 2 swallows, what is the total number of birds in the crape myrtle tree?"""
    swallows = 2
    bluebirds = swallows * 2
    cardinals = bluebirds * 3
    total_birds = swallows + bluebirds + cardinals
    result = total_birds
    return result

print(solution())