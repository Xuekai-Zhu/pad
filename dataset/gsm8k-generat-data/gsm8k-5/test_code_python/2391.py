def solution():
    candies_per_student = 4  # Lucas makes 4 pieces of chocolate candy for each of his students on Monday
    current_students = 40 // candies_per_student  # Lucas currently has enough candy for this many students
    absent_students = 3  # Three of Lucas' students will not be coming to class

    # Calculate the number of students that Lucas needs to make candy for on Monday
    remaining_students = current_students - absent_students

    # Calculate the total number of pieces of candy Lucas needs to make
    total_candies = remaining_students * candies_per_student
    result = total_candies
    return result

print(solution())