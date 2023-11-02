def solution():
    # Total number of students that can be taught at a time in the first two schools
    school_1_capacity = 400
    school_2_capacity = 400
    total_capacity_school_1_2 = school_1_capacity + school_2_capacity

    # Total number of students that can be taught at a time in the other two schools
    school_3_capacity = 340
    school_4_capacity = 340
    total_capacity_school_3_4 = school_3_capacity + school_4_capacity

    # Total number of students that can be taught at a time in all four schools
    total_capacity = total_capacity_school_1_2 + total_capacity_school_3_4
    result = total_capacity
    return result

print(solution())