def solution():
    sixth_level = 40  # Ms. Cole's sixth-level math class has 40 students
    fourth_level = 4 * sixth_level  # Ms. Cole's fourth-level math class has four times as many students as the sixth-level class
    seventh_level = 2 * fourth_level  # Ms. Cole's seventh-level math class has twice as many students as the fourth-level class

    # Calculate the total number of math students Ms. Cole teaches
    total_students = sixth_level + fourth_level + seventh_level
    result = total_students
    return result

print(solution())