def solution():
    weight_per_bushel = 56
    weight_per_ear = 0.5
    num_bushels = 2

    # Calculate the total weight of all corn picked
    total_weight = num_bushels * weight_per_bushel

    # Calculate the total number of corn ears picked
    num_ears = total_weight / weight_per_ear
    result = num_ears
    return result

print(solution())