def solution():
    sets = 2  # Elizabeth is buying 2 steak knife sets
    knives_per_set = 4  # Each set contains 4 steak knives
    total_knives = sets * knives_per_set  # Calculate the total number of steak knives

    # Calculate the cost per steak knife
    cost_per_set = 80
    cost_per_knife = cost_per_set / knives_per_set
    result = cost_per_knife
    return result

print(solution())