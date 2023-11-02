def solution():
    roman_colosseum_capacity = 87000
    allianz_parque_capacity = 44000
    madison_square_garden_attendance = 30000
    total_attendance = allianz_parque_capacity + madison_square_garden_attendance * 2
    if total_attendance <= roman_colosseum_capacity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())