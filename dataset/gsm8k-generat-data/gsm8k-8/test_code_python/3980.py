def solution():
    # Define cardinal to bluebird ratio
    c_to_b_ratio = 3

    # Calculate number of bluebirds
    num_swallows = 2
    num_bluebirds = num_swallows * 2

    # Calculate number of cardinals
    num_cardinals = num_bluebirds * c_to_b_ratio

    # Calculate total number of birds
    total_birds = num_swallows + num_bluebirds + num_cardinals
    result = total_birds
    return result

print(solution())