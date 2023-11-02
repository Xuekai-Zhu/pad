def solution():
    # Calculate the total weight of the nails
    nail_weight = 4 * 5  # 4 bags of nails, each weighing 5kg
    # Calculate the total weight of the hammers
    hammer_weight = 12 * 5  # 12 bags of hammers, each weighing 5kg
    # Calculate the maximum weight of the wooden planks that can be used
    max_plank_weight = 15 * 20 - nail_weight - hammer_weight  # 15 crates, each with max weight of 20kg, minus nail and hammer weight
    # Calculate the weight of the wooden planks used
    plank_weight = 10 * 30  # 10 bags of wooden planks, each weighing 30kg
    used_plank_weight = min(plank_weight, max_plank_weight)  # Take the lesser of the maximum plank weight or the available weight
    # Calculate the weight that needs to be left out
    left_out_weight = nail_weight + hammer_weight + (plank_weight - used_plank_weight)
    result = left_out_weight
    return result

print(solution())