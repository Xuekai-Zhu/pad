def solution():
    num_students = 35
    student_cost = 5
    num_adults = 4
    adult_cost = 6

    # Calculate the total cost for all students
    total_student_cost = num_students * student_cost

    # Calculate the total cost for all adults
    total_adult_cost = num_adults * adult_cost

    # Calculate the total cost for entrance fees for all attendees
    total_cost = total_student_cost + total_adult_cost
    result = total_cost
    return result

print(solution())