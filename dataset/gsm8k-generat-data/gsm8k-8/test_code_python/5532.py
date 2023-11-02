def solution():
    cheese_cost = 4 # cost of one kg of cheese in dollars
    veggie_cost = 6 # cost of one kg of vegetable in dollars
    cheese_weight = 8 # in kg
    veggie_weight = 7 # in kg

    cheese_total_cost = cheese_cost * cheese_weight
    veggie_total_cost = veggie_cost * veggie_weight

    total_cost = cheese_total_cost + veggie_total_cost
    result = total_cost
    return result

print(solution())