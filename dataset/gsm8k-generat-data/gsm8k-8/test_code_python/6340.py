def solution():
    # Calculate the maximum number of milkshakes that can be made
    max_milkshakes = min(72/4, 192/12)

    # Calculate the total amount of milk used for the maximum number of milkshakes
    total_milk_used = max_milkshakes * 4

    # Calculate the amount of milk left over
    milk_left = 72 - total_milk_used
    result = milk_left
    return result

print(solution())