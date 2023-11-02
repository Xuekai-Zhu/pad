def solution():
    # Calculate total revenue
    amulets_sold = 25 * 2
    revenue = amulets_sold * 40

    # Calculate total cost
    cost = amulets_sold * 30

    # Calculate faire fee
    faire_fee = revenue * 0.1

    # Calculate profit
    profit = revenue - cost - faire_fee
    result = profit
    return result

print(solution())