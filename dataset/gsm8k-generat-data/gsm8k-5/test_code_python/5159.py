def solution():
    hands_in_class = 20  # There are 20 hands in Peter's class, excluding his
    hands_per_student = 2  # Each student has 2 hands
    students_in_class = (hands_in_class / hands_per_student) + 1  # Add one for Peter's two hands
    result = students_in_class
    return result

print(solution())