def solution():
    cup_size = 12
    morning_drink = cup_size * 0.25
    office_drink = morning_drink * 0.5
    remaining = cup_size - morning_drink - office_drink - 1
    result = remaining
    return result

print(solution())