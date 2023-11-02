def solution():
    """John throws a block party and splits the cost with 3 other people. They buy 100 pounds of burgers at $3 per pound. They also buy $80 of condiments and propane to cook everything. John also buys all the alcohol which costs $200. How much did John spend altogether?"""
    burgers_cost = 100 * 3
    condiments_propane_cost = 80
    total_food_cost = burgers_cost + condiments_propane_cost
    john_alcohol_cost = 200
    total_cost = total_food_cost + john_alcohol_cost
    cost_per_person = total_cost / 4
    john_spent = cost_per_person
    result = john_spent
    return result

print(solution())