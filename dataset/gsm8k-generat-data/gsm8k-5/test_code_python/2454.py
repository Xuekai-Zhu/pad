def solution():
    total_students = 81  # There are 81 students in the classroom
    striped_students = (2/3) * total_students  # Two-thirds of the students are wearing striped shirts
    checkered_students = total_students - striped_students  # The rest are wearing checkered shirts
    shorts_students = checkered_students + 19  # There are 19 more students wearing shorts than checkered shirts

    # Calculate the difference between the number of striped students and the number of shorts students
    difference = striped_students - shorts_students
    result = difference
    return result

print(solution())