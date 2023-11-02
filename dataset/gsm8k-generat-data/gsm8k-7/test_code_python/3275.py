def solution():
    total_weight = 400
    num_parts = 8

    # Calculate the weight of one part of the cake
    part_weight = total_weight / num_parts

    # Calculate the weight of Nathalie's portion
    nathalie_portion = part_weight

    # Calculate the weight of Pierre's portion
    pierre_portion = nathalie_portion * 2
    result = pierre_portion
    return result

print(solution())