def solution():
    """Ben's new car cost twice as much as his old car. He sold his old car for $1800 and used that to pay off some of the cost of his new car. He still owes another $2000 on his new car. How much did his old car cost, in dollars?"""
    sale_price = 1800
    remaining_cost = 2000
    ratio = 1/3
    cost_of_new_car = remaining_cost / ratio
    cost_of_old_car = cost_of_new_car - sale_price
    result = cost_of_old_car
    return result

print(solution())