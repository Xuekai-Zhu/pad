def solution():
    total_students = 81
    striped_shirts_ratio = 2/3
    checkered_shirts_ratio = 1 - striped_shirts_ratio

    # Calculate the number of students wearing striped shirts
    striped_students = total_students * striped_shirts_ratio

    # Calculate the number of students wearing checkered shirts
    checkered_students = total_students * checkered_shirts_ratio

    # Calculate the number of students wearing shorts
    shorts_students = checkered_students + 19

    # Calculate the difference between the number of students wearing striped shirts and shorts
    difference = striped_students - shorts_students
    result = difference
    return result

print(solution())