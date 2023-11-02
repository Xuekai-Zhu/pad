def solution():
    # Calculate the cost of the flour
    flour_cost = (500 / 50) * 20

    # Calculate the cost of the salt
    salt_cost = 10 * 0.2

    # Calculate the total cost of the dough ball
    total_cost = flour_cost + salt_cost + 1000

    # Calculate the total revenue from ticket sales
    ticket_sales = 500 * 20

    # Calculate the profit
    profit = ticket_sales - total_cost

    result = profit
    return result

print(solution())