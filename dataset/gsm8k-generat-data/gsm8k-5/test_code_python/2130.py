def solution():
    first_course_cost = 15
    second_course_cost = first_course_cost + 5
    dessert_cost = 0.25 * second_course_cost
    total_cost = first_course_cost + second_course_cost + dessert_cost
    remaining_money = 60 - total_cost
    result = remaining_money
    return result

print(solution())