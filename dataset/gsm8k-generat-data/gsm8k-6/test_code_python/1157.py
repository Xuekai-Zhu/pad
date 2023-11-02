def solution():
    # Calculate the total weight of the clothes Tony wants to wash
    total_weight = 10 + 2*5 + 8 + 3*2  # pair of pants, 2 shirts, pair of shorts, and 3 pairs of socks

    # Calculate how much weight Tony has left to add underwear to the wash
    weight_left = 50 - total_weight

    # Calculate how many pairs of underwear Tony can add without going over the weight limit
    weight_per_underwear = 4 # weight of one pair of underwear
    pairs_of_underwear = weight_left // weight_per_underwear
    
    result = pairs_of_underwear
    return result

print(solution())