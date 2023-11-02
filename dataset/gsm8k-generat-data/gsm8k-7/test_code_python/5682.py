def solution():
    # Calculate the total cost of the suits
    suit_cost = 2 * 700

    # Calculate the total cost of the shirts
    shirt_cost = 6 * 50

    # Calculate the total cost of the loafers
    loafer_cost = 2 * 150

    # Calculate the total cost of all clothing items
    total_cost = suit_cost + shirt_cost + loafer_cost

    # Calculate Enrique's commission
    commission_rate = 0.15
    commission = commission_rate * total_cost
    result = commission
    return result

print(solution())