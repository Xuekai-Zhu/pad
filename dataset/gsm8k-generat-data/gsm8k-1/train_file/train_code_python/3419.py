def solution():
    """Jimmy has a collection of 5 action figures. Each figure is worth $15, except for one which is worth $20. He decided to sell his collection. To do it fast he decided to sell each of them for $5 less than their value. How much will Jimmy earn if he sells all the figures?"""
    total_figures = 5
    regular_price = 15
    expensive_price = 20
    discount = 5
    total_regular_price = (total_figures - 1) * regular_price
    total_expensive_price = expensive_price
    total_sale_price = (total_figures * (regular_price - discount)) + (expensive_price - discount)
    total_earnings = total_sale_price - (total_regular_price + total_expensive_price)
    result = total_earnings
    return result

print(solution())