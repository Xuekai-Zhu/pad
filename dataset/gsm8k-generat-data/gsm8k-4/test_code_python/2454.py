def solution():
    """In a classroom of 81 students, two-thirds are wearing striped shirts while the others are wearing checkered shirts. If there are 19 more students wearing shorts than checkered shirts, how many more students are wearing striped shirts than shorts?"""
    # Define the total number of students and the proportion wearing striped shirts
    total_students = 81
    striped_proportion = 2/3

    # Calculate the number of students wearing striped shirts and checkered shirts
    striped_students = total_students * striped_proportion
    checkered_students = total_students - striped_students

    # Calculate the number of students wearing shorts
    shorts_students = checkered_students + 19

    # Calculate the difference in the number of students wearing striped shirts and shorts
    difference = striped_students - shorts_students

    # return the result
    result = difference
    return result

print(solution())