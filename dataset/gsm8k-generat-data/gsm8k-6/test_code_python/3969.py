def solution():
    # Calculate the extra minutes of recess earned by the students
    extra_minutes = (10 * 2) + (12 * 1) + (0 * 14) - (5 * 1)  # 10 As earn 20 extra minutes, 12 Bs earn 12 extra minutes, 14 Cs earn 0 extra minutes, 5 Ds earn 5 fewer minutes
    total_recess = 20 + extra_minutes  # add the extra minutes to the normal 20 minutes of recess

    result = total_recess
    return result

print(solution())