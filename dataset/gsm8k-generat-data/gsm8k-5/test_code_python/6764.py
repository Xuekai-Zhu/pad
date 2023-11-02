def solution():
    # Calculate the total number of students
    students_per_group = 6  # Each group has 6 students (5+1)
    total_students = students_per_group * 5  # There are 5 groups in total

    # Calculate the total number of sandwiches needed
    sandwiches_per_student = 2  # Each student needs 2 sandwiches
    total_sandwiches = total_students * sandwiches_per_student

    # Calculate the total number of pieces of bread needed
    pieces_of_bread_per_sandwich = 2  # Each sandwich needs 2 pieces of bread
    total_pieces_of_bread = total_sandwiches * pieces_of_bread_per_sandwich
    result = total_pieces_of_bread
    return result

print(solution())