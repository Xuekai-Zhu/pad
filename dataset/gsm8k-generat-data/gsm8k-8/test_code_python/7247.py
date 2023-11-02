def solution():
    # Define variables and equations
    total_attendance = 2700
    first_day = x
    second_day = 0.5 * first_day
    third_day = 3 * first_day
    equation = first_day + second_day + third_day - total_attendance

    # Solve for first_day using the equation
    first_day = optimize.brentq(lambda x: equation, 0, total_attendance)

    # Calculate attendance for second day
    second_day = 0.5 * first_day

    result = second_day
    return result

print(solution())