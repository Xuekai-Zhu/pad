def solution():
    # Calculate the weight of marble carved off the statues
    marble_carved_off = 22

    # Calculate the weight of the first two statues and the remaining marble
    total_weight_first_two = 10 + 18
    remaining_weight_marble = 80 - total_weight_first_two - marble_carved_off

    # Calculate the weight of each remaining statue
    weight_each_remaining = remaining_weight_marble / 2
    result = weight_each_remaining
    return result

print(solution())