def solution():
    third_grade_classes = 5
    fourth_grade_classes = 4
    fifth_grade_classes = 4
    third_grade_students = 30
    fourth_grade_students = 28
    fifth_grade_students = 27
    hamburger_cost = 2.10
    carrot_cost = 0.50
    cookie_cost = 0.20
    total_cost = ((third_grade_classes * third_grade_students) + (fourth_grade_classes * fourth_grade_students) + (fifth_grade_classes * fifth_grade_students)) * (hamburger_cost + carrot_cost + cookie_cost)
    result = total_cost
    return result

print(solution())