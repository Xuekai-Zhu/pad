def solution():
    # Calculate the cost of 1 apple
    apple_cost = 3/2

    # Calculate the selling price of 1 apple
    apple_price = 10/5

    # Calculate the profit on 5 apples
    apple_profit = (apple_price - apple_cost) * 5

    # Calculate the profit on 5 oranges
    orange_profit = (1 - (2.7/3)) * 5

    # Calculate the total profit
    total_profit = apple_profit + orange_profit

    result = total_profit
    return result

print(solution())