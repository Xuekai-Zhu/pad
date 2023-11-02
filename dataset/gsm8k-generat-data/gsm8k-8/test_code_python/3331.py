def solution():
    # Convert the weight limit to ounces
    weight_limit = 20 * 16

    # Calculate the total weight of the plates in ounces
    total_weight = 38 * 10

    # Keep removing 10 ounces at a time until total weight is within the limit
    plates_removed = 0
    while total_weight > weight_limit:
        total_weight -= 10
        plates_removed += 1

    result = plates_removed
    return result

print(solution())