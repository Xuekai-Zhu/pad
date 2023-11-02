def solution():
    """In a classroom of 81 students, two-thirds are wearing striped shirts while the others are wearing checkered shirts. If there are 19 more students wearing shorts than checkered shirts, how many more students are wearing striped shirts than shorts?"""
    # Calculate the number of students wearing striped shirts
    striped = 81 * (2/3)

    # Calculate the number of students wearing checkered shirts
    checkered = 81 - striped

    # Calculate the number of students wearing shorts
    shorts = checkered + 19

    # Calculate the difference between the number of students wearing striped shirts and shorts
    difference = striped - shorts

    # Display the difference
    result = difference
    return result

print(solution())