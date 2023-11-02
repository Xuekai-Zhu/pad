def solution():
    num_students_before_intersection = 28
    num_students_after_intersection = 58

    # Calculate the number of students who entered the bus at the intermediate stop
    num_students_at_intersection = num_students_after_intersection - num_students_before_intersection

    # Calculate 40% of the number of students who entered at the intermediate stop
    forty_percent = 0.40
    num_students_40_percent = num_students_at_intersection * forty_percent

    result = num_students_40_percent
    return result

print(solution())