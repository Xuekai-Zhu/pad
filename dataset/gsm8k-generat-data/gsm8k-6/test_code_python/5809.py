def solution():
    # Calculate the weight of all the items Daryl has to load
    total_weight = (4 * 5) + (12 * 5) + (10 * 30)  # weight of nails + weight of hammers + weight of wooden planks
    max_weight = 20 * 15  # weight limit of the crates

    # Calculate the weight Daryl needs to leave out
    excess_weight = total_weight - max_weight
    result = excess_weight
    return result

print(solution())