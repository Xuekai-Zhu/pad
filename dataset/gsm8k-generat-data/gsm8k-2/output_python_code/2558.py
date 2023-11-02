def solution():
    """Ben's new car cost twice as much as his old car. He sold his old car for $1800 and used that to pay off some of the cost of his new car. He still owes another $2000 on his new car. How much did his old car cost, in dollars?"""
    selling_price = 1800
    remaining_cost = 2000
    new_car_cost = selling_price + remaining_cost
    old_car_cost = new_car_cost / 3
    result = old_car_cost
    return result

print(solution())