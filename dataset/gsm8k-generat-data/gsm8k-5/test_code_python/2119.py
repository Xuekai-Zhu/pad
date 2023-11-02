def solution():
    total_oranges = 108  # There were 108 oranges to be shared
    num_students = 12  # There were 12 students in the class
    bad_oranges = 36  # 36 oranges were bad and had to be thrown away

    # Calculate the number of good oranges left after throwing away the bad ones
    good_oranges = total_oranges - bad_oranges

    # Calculate the number of oranges each student would have gotten if no orange had to be thrown away
    oranges_per_student_without_waste = total_oranges / num_students

    # Calculate the number of oranges each student will get now that some oranges had to be thrown away
    oranges_per_student_with_waste = good_oranges / num_students

    # Calculate the difference between the two amounts
    difference = oranges_per_student_without_waste - oranges_per_student_with_waste
    result = difference
    return result

print(solution())