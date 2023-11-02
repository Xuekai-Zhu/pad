def solution():
    num_students = 12
    total_oranges = 108
    bad_oranges = 36

    # Calculate the total number of good oranges
    good_oranges = total_oranges - bad_oranges

    # Calculate the number of oranges each student would have received if none were thrown away
    num_oranges_per_student_without_waste = total_oranges // num_students

    # Calculate the number of oranges each student will receive now
    num_oranges_per_student_with_waste = good_oranges // num_students

    # Calculate the difference in the number of oranges each student will receive
    difference = num_oranges_per_student_without_waste - num_oranges_per_student_with_waste
    result = difference
    return result

print(solution())