def solution():
    # Define initial enrollment
    enrollment = 8

    # Advertising brings in 8 more students
    enrollment += 8

    # One fourth of the new students drop out
    enrollment -= int(0.25 * 8)

    # 2 more students drop out
    enrollment -= 2

    # Enrollment increases by 5 times the original number of students
    enrollment += 5 * 8

    # 2 students drop out due to scheduling conflicts
    enrollment -= 2

    # Another rally brings in 6 more students
    enrollment += 6

    # Half of the class drops out
    enrollment = int(0.5 * enrollment)

    # Half of the remaining students graduate
    enrollment = int(0.5 * enrollment)

    result = enrollment
    return result

print(solution())