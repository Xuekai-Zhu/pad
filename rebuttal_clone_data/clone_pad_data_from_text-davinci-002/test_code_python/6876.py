$\

def solution():
    tip = 99
    cost_of_steak = 24
    cost_of_burgers = 3.5
    cost_of_ice_cream = 2
    number_of_steak_meals = 2
    number_of_burgers = 2
    number_of_ice_cream = 3
    total_cost = (cost_of_steak * number_of_steak_meals) + (cost_of_burgers * number_of_burgers) + (cost_of_ice_cream * number_of_ice_cream)
    money_left = tip - total_cost
    result = money_left
    return result

print(solution())