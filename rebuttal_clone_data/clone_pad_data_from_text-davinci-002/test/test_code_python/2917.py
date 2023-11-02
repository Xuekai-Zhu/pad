def solution():
    appetizer = 9.00
    entree = 20.00
    dessert = 11.00
    tip = 30
    total = appetizer + (2*entree) + dessert + ((tip/100)*(appetizer+(2*entree)+dessert))
    result = total
    return result

print(solution())