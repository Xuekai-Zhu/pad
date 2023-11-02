def solution():
    # Calculate the total number of students in the school
    total_third_graders = 5 * 30
    total_fourth_graders = 4 * 28
    total_fifth_graders = 4 * 27
    total_students = total_third_graders + total_fourth_graders + total_fifth_graders

    # Calculate the total cost of one lunch for all the students
    hamburger_cost = total_students * 2.10
    carrot_cost = total_students * 0.50
    cookie_cost = total_students * 0.20
    total_cost = hamburger_cost + carrot_cost + cookie_cost
    result = total_cost
    return result

print(solution())