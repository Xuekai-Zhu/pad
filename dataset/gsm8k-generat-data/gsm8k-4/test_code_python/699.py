def solution():
    """Marla is planning the lunch menu for an elementary school. There are 5 third grade classes with 30 students each, 4 fourth grade classes with 28 students each, and 4 fifth grade classes with 27 students each. Each student gets a hamburger, which costs $2.10, some carrots, which cost $0.50, and a cookie, which cost $0.20. How much does one lunch for all the students cost?"""
    # Define the number of students in each grade
    third_grade_students = 5 * 30
    fourth_grade_students = 4 * 28
    fifth_grade_students = 4 * 27

    # Calculate the total number of students
    total_students = third_grade_students + fourth_grade_students + fifth_grade_students

    # Calculate the cost of one lunch for all the students
    hamburger_cost = total_students * 2.1
    carrot_cost = total_students * 0.5
    cookie_cost = total_students * 0.2
    total_cost = hamburger_cost + carrot_cost + cookie_cost

    # return the result
    result = total_cost
    return result

print(solution())