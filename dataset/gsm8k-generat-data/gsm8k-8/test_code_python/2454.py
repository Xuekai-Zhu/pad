def solution():
    # Calculate the number of students wearing striped shirts
    striped_students = 81 * (2/3)

    # Calculate the number of students wearing checkered shirts
    checkered_students = 81 - striped_students

    # Calculate the number of students wearing shorts
    shorts_students = checkered_students + 19

    # Calculate the difference between the number of students wearing striped shirts and shorts
    difference = striped_students - shorts_students

    result = difference
    return result

print(solution())