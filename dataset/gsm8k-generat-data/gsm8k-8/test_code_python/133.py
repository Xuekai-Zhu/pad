def solution():
    # Calculate the number of students absent
    absent = 40 * (1/10)

    # Calculate the number of students present
    present = 40 - absent

    # Calculate the number of students in the classroom
    in_class = present * (3/4)

    # Calculate the number of students in the canteen
    in_canteen = present - in_class
    result = in_canteen
    return result

print(solution())