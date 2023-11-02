def solution():
    # Define the weight of the cake and the number of parts
    cake_weight = 400
    num_parts = 8

    # Define Nathalie's share and Pierre's share
    nathalie_share = cake_weight / num_parts
    pierre_share = nathalie_share * 2

    result = pierre_share
    return result

print(solution())