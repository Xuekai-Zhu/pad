def solution():
    
    third_grade_students = 5 * 30
    fourth_grade_students = 4 * 28
    fifth_grade_students = 4 * 27
    total_students = third_grade_students + fourth_grade_students + fifth_grade_students

    hamburger_cost = total_students * 2.10
    carrot_cost = total_students * 0.50
    cookie_cost = total_students * 0.20

    total_cost = hamburger_cost + carrot_cost + cookie_cost

    result = total_cost
    return result

print(solution())