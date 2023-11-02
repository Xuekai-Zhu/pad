def solution():
    sugar_weight = 16 # kg
    salt_weight = 30 # kg
    total_weight = sugar_weight + salt_weight # kg
    removed_weight = 4 # kg

    # Calculate the new weight of the bags after removing 4 kg from the total weight
    new_total_weight = total_weight - removed_weight
    result = new_total_weight
    return result

print(solution())