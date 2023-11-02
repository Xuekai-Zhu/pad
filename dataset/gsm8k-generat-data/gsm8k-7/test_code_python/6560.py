def solution():
    total_fruit_weight = 8 # pounds
    mario_oranges_weight = 0.5 # pounds (converted 8 ounces to pounds)
    lydia_apples_weight = 1.5 # pounds (converted 24 ounces to pounds)

    # Calculate the weight of peaches eaten by Nicolai
    nicolai_peaches_weight = total_fruit_weight - mario_oranges_weight - lydia_apples_weight

    result = nicolai_peaches_weight
    return result

print(solution())