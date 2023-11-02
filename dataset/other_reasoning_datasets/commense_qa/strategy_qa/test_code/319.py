def solution():
    daily_sodium_limit = 2300
    sodium_in_half_cup_olives = 735
    if sodium_in_half_cup_olives <= daily_sodium_limit:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())