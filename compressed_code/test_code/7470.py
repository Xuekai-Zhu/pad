def solution():
    
    total_budget = 60
    first_course = 15
    second_course = first_course + 5
    dessert = 0.25 * second_course
    total_spent = first_course + second_course + dessert
    money_left = total_budget - total_spent
    result = money_left
    return result

print(solution())