def solution():
    # Define the initial weights of the sugar and salt bags
    sugar_weight = 16
    salt_weight = 30

    # Calculate the combined weight before removing 4 kg
    combined_weight = sugar_weight + salt_weight

    # Subtract 4 kg from the combined weight
    new_weight = combined_weight - 4

    result = new_weight
    return result

print(solution())