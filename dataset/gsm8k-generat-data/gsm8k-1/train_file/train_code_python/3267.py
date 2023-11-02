def solution():
    """Romeo buys five bars of chocolate at $5 each and sells these chocolates for a total of $90. If he uses packaging material that costs him $2 for each bar of chocolate, how much profit does he make for all the chocolates he sells?"""
    cost_per_chocolate = 5 + 2 # cost of chocolate plus packaging material 
    total_cost = cost_per_chocolate * 5 # buying 5 bars
    total_sales = 90
    profit = total_sales - total_cost
    result = profit
    return result

print(solution())