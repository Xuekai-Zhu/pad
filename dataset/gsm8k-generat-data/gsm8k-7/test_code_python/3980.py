def solution():
    num_swallows = 2
    num_bluebirds = num_swallows * 2  # half as many as bluebirds
    num_cardinals = num_bluebirds * 3  # three times more than bluebirds

    # Calculate the total number of birds
    total_birds = num_swallows + num_bluebirds + num_cardinals
    result = total_birds
    return result

print(solution())