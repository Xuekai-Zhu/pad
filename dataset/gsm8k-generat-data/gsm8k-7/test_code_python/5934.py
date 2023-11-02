def solution():
    num_level_six_students = 40
    num_level_four_students = num_level_six_students * 4
    num_level_seven_students = num_level_four_students * 2

    # Calculate the total number of math students that Ms. Cole teaches
    total_num_students = num_level_six_students + num_level_four_students + num_level_seven_students
    result = total_num_students
    return result

print(solution())