def solution():
    # Calculate Jamison's weight
    jamison_weight = 160 + 20

    # Calculate John's weight
    john_weight = (1/4 * mary_weight) + mary_weight

    # Calculate the total weight
    total_weight = jamison_weight + mary_weight + john_weight
    result = total_weight
    return result

print(solution())