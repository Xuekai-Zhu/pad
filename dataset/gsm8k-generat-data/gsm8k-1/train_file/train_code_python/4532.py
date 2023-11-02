def solution():
    """Mike decides to develop a plot of land. He bought 200 acres for $70 per acre. After development, he sold half of the acreage for $200 per acre. How much profit did he make?"""
    acres_bought = 200
    initial_cost = acres_bought * 70
    acres_sold = acres_bought / 2
    sale_price = acres_sold * 200
    development_cost = initial_cost / 2
    profit = sale_price - (initial_cost + development_cost)
    result = profit
    return result

print(solution())