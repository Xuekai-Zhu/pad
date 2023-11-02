def solution():
    total_students = 50  # There are 50 students in the school
    free_lunch_students = 0.4 * total_students  # 40% of the students receive a free lunch
    paying_students = total_students - free_lunch_students  # The rest of the students pay for their lunch
    total_cost = 210  # The total cost of feeding all the students is $210

    # Calculate the cost per paying student
    cost_per_paying_student = total_cost / paying_students
    result = cost_per_paying_student
    return result

print(solution())