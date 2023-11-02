def solution():
    appetizer = 8
    entrée = 20
    wine = 3
    dessert = 6
    discount = entrée / 2
    total_cost = appetizer + entrée + (wine * 2) + dessert - discount
    tip = total_cost * 0.2
    result = total_cost + tip
    return result

print(solution())