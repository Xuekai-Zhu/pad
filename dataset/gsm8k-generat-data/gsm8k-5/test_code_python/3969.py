def solution():
    # Calculate the extra minutes of recess each grade receives
    extra_A = 2
    extra_B = 1
    extra_C = 0
    extra_D = -1

    # Calculate the total extra minutes of recess earned by each grade
    total_extra_A = 10 * extra_A
    total_extra_B = 12 * extra_B
    total_extra_C = 14 * extra_C
    total_extra_D = 5 * extra_D

    # Calculate the total extra minutes of recess earned by all the students
    total_extra_recess = total_extra_A + total_extra_B + total_extra_C + total_extra_D

    # Calculate the total recess time, including the extra minutes earned by the students
    total_recess = 20 + total_extra_recess
    result = total_recess
    return result

print(solution())