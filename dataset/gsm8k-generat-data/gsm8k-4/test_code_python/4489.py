def solution():
    """Michael has $50. He wants to surprise his mom on Mother's day by buying a cake for $20, a bouquet for $36, and a set of balloons for $5. How much more money does Michael need to buy all those?"""
    # Define the cost of the cake, bouquet, and balloons
    cake_cost = 20
    bouquet_cost = 36
    balloons_cost = 5

    # Calculate the total cost of the items
    total_cost = cake_cost + bouquet_cost + balloons_cost

    # Calculate the amount of money Michael still needs to buy all the items
    remaining_money = total_cost - 50

    result = remaining_money
    return result

print(solution())