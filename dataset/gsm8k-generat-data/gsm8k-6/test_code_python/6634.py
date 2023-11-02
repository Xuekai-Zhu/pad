def solution():
    # Calculate the total number of students at the school
    total_students = 300 / (1 - 0.6)  # number of boys divided by the percentage of boys (40%) gives the total number of students
    # Calculate the number of girls at the school
    girls = total_students * 0.6  # 60% of the total number of students are girls
    result = girls
    return result

print(solution())