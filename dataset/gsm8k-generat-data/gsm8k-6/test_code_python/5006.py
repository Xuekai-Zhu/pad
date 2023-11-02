def solution():
    # Calculate the total cost of the candy
    total_cost = 20 - 11  # James pays with a $20 bill and gets $11 change
    num_packs = 3  # James buys 3 packs of candy

    # Calculate the cost of each pack of candy
    cost_per_pack = total_cost / num_packs
    result = cost_per_pack
    return result

print(solution())