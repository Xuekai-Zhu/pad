def solution():
    # Let's call the number of students in Tina and Maura's class "x":
    x = 22 * 2

    # Zack's classroom has half the amount of total students between Tina and Maura's classrooms:
    z = (x + x) / 2

    # The total number of students is the sum of all three classrooms:
    total_students = x + x + z
    result = total_students
    return result

print(solution())