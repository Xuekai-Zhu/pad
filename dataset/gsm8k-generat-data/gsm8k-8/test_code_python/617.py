def solution():
    # Calculate the base fine
    base_fine = 50

    # Calculate the additional fine based on Mark's speed
    extra_fine = (75 - 30) * 2

    # Calculate the total fine
    total_fine = (base_fine + extra_fine) * 2

    # Calculate the total cost including court and lawyer fees
    total_cost = total_fine + 300 + (80 * 3)

    result = total_cost
    return result

print(solution())