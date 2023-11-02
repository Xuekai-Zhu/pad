def solution():
    """Janet buys 3 pounds of broccoli for $4 a pound, 3 oranges for $0.75 each, a cabbage for $3.75, a pound of bacon for $3, and two pounds of chicken for $3 a pound. What percentage of her grocery budget did she spend on meat, rounded to the nearest percent?"""
    broccoli_cost = 3 * 4
    orange_cost = 3 * 0.75
    cabbage_cost = 3.75
    bacon_cost = 3
    chicken_cost = 2 * 3
    total_cost = broccoli_cost + orange_cost + cabbage_cost + bacon_cost + chicken_cost
    meat_cost = bacon_cost + chicken_cost
    meat_percentage = (meat_cost / total_cost) * 100
    result = round(meat_percentage)
    return result

print(solution())