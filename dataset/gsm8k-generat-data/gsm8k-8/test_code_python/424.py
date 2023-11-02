def solution():
    initial_rice = 10000 # 10 kg = 10000 g
    morning_cooked_rice = initial_rice * (9/10)
    remaining_rice = initial_rice - morning_cooked_rice
    evening_cooked_rice = remaining_rice * (1/4)
    left_over_rice = remaining_rice - evening_cooked_rice
    result = left_over_rice # in grams
    return result

print(solution())