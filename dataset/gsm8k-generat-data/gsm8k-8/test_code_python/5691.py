def solution():
    # Calculate the total cost of the meal before discount or tip
    total_cost = 8 + 20 + (2 * 3) + 6

    # Apply the half-off voucher to the entrée cost
    entrée_cost = 20 * 0.5

    # Calculate the full cost of the meal without discount, but with the half-off entrée
    full_cost = 8 + entrée_cost + (2 * 3) + 6

    # Calculate the amount of the tip based on the full cost
    tip = full_cost * 0.20

    # Calculate the total cost of the meal including the tip
    total_with_tip = full_cost + tip

    return total_with_tip

print(solution())