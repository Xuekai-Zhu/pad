def solution():
    human_stomach_capacity = 4
    bull_food_consumption = 33
    moose_weight = 1500
    minotaur_capacity = (human_stomach_capacity * 2) + bull_food_consumption
    if minotaur_capacity < moose_weight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())