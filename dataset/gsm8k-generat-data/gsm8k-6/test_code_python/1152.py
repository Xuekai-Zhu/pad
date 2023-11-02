def solution():
    # Calculate the total number of students before adding 5 more classes
    total_students = 15 * 20

    # Calculate the total number of students after adding 5 more classes
    new_total_students = (15 + 5) * 20

    # Calculate the increase in number of students
    increase = new_total_students - total_students

    result = increase
    return result

print(solution())