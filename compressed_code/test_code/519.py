def solution():
    
    third_grade_students = 5 * 30
    fourth_grade_students = 4 * 28
    fifth_grade_students = 4 * 27
    total_students = third_grade_students + fourth_grade_students + fifth_grade_students
    burger_cost = 2.10
    carrot_cost = 0.50
    cookie_cost = 0.20
    total_cost_per_student = burger_cost + carrot_cost + cookie_cost
    total_cost = total_cost_per_student * total_students
    result = total_cost
    return result

print(solution())