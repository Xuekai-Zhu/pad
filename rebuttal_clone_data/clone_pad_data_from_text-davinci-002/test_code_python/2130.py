def solution():
    money = 60
    first_course = 15
    second_course = first_course + 5
    dessert = second_course * 0.25
    total_cost = first_course + second_course + dessert
    money_left = money - total_cost
    result = money_left
    return result

print(solution())