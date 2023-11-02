def solution():
    # Calculate the total number of students that can be taught in the first two schools
    school1_capacity = 400
    school2_capacity = 400
    total_capacity1 = school1_capacity + school2_capacity

    # Calculate the total number of students that can be taught in the last two schools
    school3_capacity = 340
    school4_capacity = 340
    total_capacity2 = school3_capacity + school4_capacity

    # Calculate the total number of students that can be taught in all four schools
    total_capacity = total_capacity1 + total_capacity2

    result = total_capacity
    return result

print(solution())