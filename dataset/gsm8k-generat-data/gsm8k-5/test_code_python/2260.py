def solution():
    total_students = 180  # There are 180 students in total
    deaf_to_blind_ratio = 3  # The deaf-student population is 3 times the blind-student population

    # Let x be the number of blind students
    x = total_students / (deaf_to_blind_ratio + 1 + deaf_to_blind_ratio * 3)

    result = x
    return result

print(solution())