def solution():
    
    sandwich_cost = 8
    discount = 0.25
    avocado_cost = 1
    drink_and_salad_cost = 12 - (sandwich_cost - (sandwich_cost * discount)) - avocado_cost
    drink_cost = drink_and_salad_cost - 3
    result = drink_cost
    return result

print(solution())