def solution():
    # Calculate the number of oil changes per year
    oil_changes = 1000 * 12 // 3000 + 1  # double slashes represent integer division, adding 1 for the free oil change

    # Calculate the cost of oil changes per year
    oil_change_cost = (oil_changes - 1) * 50  # subtracting 1 for the free oil change

    result = oil_change_cost
    return result

print(solution())