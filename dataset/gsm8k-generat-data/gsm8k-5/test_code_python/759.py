def solution():
    # Calculate the cost of the flour
    flour_cost = (500 / 50) * 20  # 500 pounds of flour, 50-pound bags, and $20 per bag

    # Calculate the cost of the salt
    salt_cost = 10 * 0.2  # 10 pounds of salt, $0.2 per pound

    # Calculate the total cost
    total_cost = flour_cost + salt_cost + 1000  # Add the cost of promoting

    # Calculate the revenue from ticket sales
    revenue = 500 * 20  # 500 tickets sold, $20 per ticket

    # Calculate the profit
    profit = revenue - total_cost
    result = profit
    return result

print(solution())