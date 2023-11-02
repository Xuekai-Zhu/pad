def solution():
    ingredient_cost = 20  # cost of ingredients
    profit = 80  # desired profit
    cup_cost = 2  # cost per cup
    cups_sold = (profit + ingredient_cost) / cup_cost  # calculate the number of cups sold
    result = cups_sold
    return result

print(solution())