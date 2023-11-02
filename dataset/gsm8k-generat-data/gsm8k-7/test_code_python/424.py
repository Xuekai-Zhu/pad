def solution():
    initial_amount = 10000 # 10 kilograms in grams
    morning_cooked = initial_amount * (9/10)
    remaining = initial_amount - morning_cooked
    evening_cooked = remaining * (1/4)
    remaining = remaining - evening_cooked
    result = remaining
    return result

print(solution())