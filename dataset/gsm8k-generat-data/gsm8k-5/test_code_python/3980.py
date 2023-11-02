def solution():
    swallows = 2  # Given
    bluebirds = swallows * 2  # Half as many swallows as bluebirds
    cardinals = bluebirds * 3  # Three times more cardinals than bluebirds

    # Calculate the total number of birds
    total_birds = swallows + bluebirds + cardinals
    result = total_birds
    return result

print(solution())