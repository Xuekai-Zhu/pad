def solution():
    # Find the number of students in the fourth-level class
    fourth_level = 4 * 40

    # Find the number of students in the seventh-level class
    seventh_level = 2 * fourth_level

    # Calculate the total number of math students
    total_students = 40 + fourth_level + seventh_level

    result = total_students
    return result

print(solution())