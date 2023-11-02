def solution():
    num_third_grade_classes = 5
    third_grade_class_size = 30

    num_fourth_grade_classes = 4
    fourth_grade_class_size = 28

    num_fifth_grade_classes = 4
    fifth_grade_class_size = 27

    hamburger_cost = 2.10
    carrot_cost = 0.50
    cookie_cost = 0.20

    # Calculate the total number of students
    total_students = (num_third_grade_classes * third_grade_class_size) + \
                     (num_fourth_grade_classes * fourth_grade_class_size) + \
                     (num_fifth_grade_classes * fifth_grade_class_size)

    # Calculate the total cost of all hamburgers
    total_hamburger_cost = total_students * hamburger_cost

    # Calculate the total cost of all carrots
    total_carrot_cost = total_students * carrot_cost

    # Calculate the total cost of all cookies
    total_cookie_cost = total_students * cookie_cost

    # Calculate the total cost of one lunch for all the students
    total_lunch_cost = total_hamburger_cost + total_carrot_cost + total_cookie_cost
    result = total_lunch_cost
    return result

print(solution())