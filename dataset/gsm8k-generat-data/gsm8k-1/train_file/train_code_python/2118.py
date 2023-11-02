def solution():
    """A class of 12 students was about to share 108 oranges equally among themselves when it was discovered that 36 of the oranges were bad and had to be thrown away. How many oranges less will each student get now than if no orange had to be thrown away?"""
    num_students = 12
    total_oranges = 108
    bad_oranges = 36
    good_oranges = total_oranges - bad_oranges
    oranges_per_student_without_waste = total_oranges // num_students
    oranges_per_student_with_waste = good_oranges // num_students
    difference = oranges_per_student_without_waste - oranges_per_student_with_waste
    result = difference
    return result

print(solution())