def solution():
    sugar_weight = 16
    salt_weight = 30
    remove_weight = 4

    # Calculate the combined weight of the bags
    combined_weight = sugar_weight + salt_weight

    # Remove the weight from the combined weight
    new_combined_weight = combined_weight - remove_weight

    # Divide the new combined weight equally between the bags
    new_sugar_weight = new_combined_weight / 2
    new_salt_weight = new_combined_weight / 2

    result = (new_sugar_weight, new_salt_weight)
    return result

print(solution())