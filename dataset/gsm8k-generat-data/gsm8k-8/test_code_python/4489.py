def solution():
    # Define Michael's initial amount of money
    michael_money = 50

    # Define the cost of the cake, bouquet, and balloons
    cake_cost = 20
    bouquet_cost = 36
    balloons_cost = 5

    # Calculate the total cost of the items
    total_cost = cake_cost + bouquet_cost + balloons_cost

    # Calculate how much more money Michael needs
    more_money_needed = total_cost - michael_money
    result = more_money_needed
    return result

print(solution())