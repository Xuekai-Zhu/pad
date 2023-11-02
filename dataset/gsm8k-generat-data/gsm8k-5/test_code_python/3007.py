def solution():
    total_spent = 50  # Emily spent a total of $50
    art_supplies_cost = 20  # Emily bought art supplies for $20
    skirts_cost = (total_spent - art_supplies_cost) / 2  # The cost of 2 skirts is the difference between the total spent and the art supplies cost, divided by 2

    result = skirts_cost
    return result

print(solution())