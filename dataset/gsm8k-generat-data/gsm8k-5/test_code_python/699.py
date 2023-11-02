def solution():
    third_grade_students = 5 * 30  # There are 5 third grade classes with 30 students each
    fourth_grade_students = 4 * 28  # There are 4 fourth grade classes with 28 students each
    fifth_grade_students = 4 * 27  # There are 4 fifth grade classes with 27 students each
    total_students = third_grade_students + fourth_grade_students + fifth_grade_students

    hamburger_cost = 2.10
    carrots_cost = 0.50
    cookie_cost = 0.20
    total_cost_per_student = hamburger_cost + carrots_cost + cookie_cost

    # Calculate the total cost for all the lunches
    total_cost = total_students * total_cost_per_student
    result = total_cost
    return result

print(solution())