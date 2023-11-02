def solution():
    # Define the number of students in Ms. Cole's sixth-level class
    sixth_level_students = 40

    # Calculate the number of students in Ms. Cole's fourth-level class
    fourth_level_students = 4 * sixth_level_students

    # Calculate the number of students in Ms. Cole's seventh-level class
    seventh_level_students = 2 * fourth_level_students

    # Calculate the total number of math students Ms. Cole teaches
    total_students = sixth_level_students + fourth_level_students + seventh_level_students
    result = total_students
    return result

print(solution())