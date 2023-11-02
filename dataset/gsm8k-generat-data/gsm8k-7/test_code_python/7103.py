def solution():
    single_balloon_price = 0.5
    pack_balloon_price = 3
    pack_size = 10
    total_balloons = 14

    # Calculate the number of packs needed to get the best deal
    num_packs = total_balloons // pack_size

    # Calculate the total cost of the packs
    total_pack_cost = num_packs * pack_balloon_price

    # Calculate the number of single balloons needed to complete the order
    remaining_balloons = total_balloons % pack_size

    # Calculate the total cost of the remaining single balloons
    total_single_cost = remaining_balloons * single_balloon_price

    # Calculate the total cost of all the balloons
    total_cost = total_pack_cost + total_single_cost
    result = total_cost
    return result

print(solution())