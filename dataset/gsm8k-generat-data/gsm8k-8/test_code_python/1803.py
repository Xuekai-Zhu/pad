def solution():
    # Total number of students in period 5
    total_students = 90

    # Number of students in the cafeteria initially
    cafeteria_initial = total_students * (2/3)

    # Number of students outside initially
    outside_initial = total_students * (1/3)

    # Number of students who jumped inside
    jumped_inside = outside_initial * (1/3)

    # Number of students who went outside
    went_outside = 3

    # Calculate the final number of students in the cafeteria
    cafeteria_final = cafeteria_initial + jumped_inside - went_outside
    result = cafeteria_final
    return result

print(solution())