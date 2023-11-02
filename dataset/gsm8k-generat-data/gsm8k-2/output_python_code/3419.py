def solution():
    """Jimmy has a collection of 5 action figures. Each figure is worth $15, except for one which is worth $20. He decided to sell his collection. To do it fast he decided to sell each of them for $5 less than their value. How much will Jimmy earn if he sells all the figures?"""
    figure_count = 5
    standard_price = 15
    special_price = 20
    discount_price = standard_price - 5
    total_cost = (figure_count - 1) * standard_price + special_price
    total_price = figure_count * discount_price
    profit = total_price - total_cost
    result = profit
    return result

print(solution())