def solution():
    # Calculate the cost per apple
    apple_cost = 3 / 2

    # Calculate the selling price per apple
    apple_price = 10 / 5

    # Calculate the cost per orange
    orange_cost = 2.7 / 3

    # Calculate the selling price per orange
    orange_price = 1

    # Calculate the total cost of 5 apples and 5 oranges
    total_cost = (5 * apple_cost) + (5 * orange_cost)

    # Calculate the total revenue from selling 5 apples and 5 oranges
    total_revenue = (5 * apple_price) + (5 * orange_price)

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())