def solution():
    
    total_money = 60
    first_course_cost = 15
    second_course_cost = 20
    dessert_cost = 0.25 * second_course_cost
    total_cost = first_course_cost + second_course_cost + dessert_cost
    remaining_money = total_money - total_cost
    result = remaining_money
    return result

print(solution())