def solution():
    shirts_per_pound = 4  # 4 shirts weigh 1 pound
    pants_per_pound = 2  # 2 pairs of pants weigh 1 pound
    total_shirts = 20
    total_pants = 20
    total_weight = (total_shirts / shirts_per_pound) + (total_pants / pants_per_pound)

    # Calculate the number of loads Jon needs to do
    num_loads = total_weight / 5

    result = num_loads
    return result

print(solution())