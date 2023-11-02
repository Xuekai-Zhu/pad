def solution():
    """If there were 200 students who passed an English course three years ago, and each subsequent year until the current one that number increased by 50% of the previous year's number, how many students will pass the course this year?"""
    # Define the initial number of students who passed the course
    students_passed = 200

    # Calculate the number of students who passed the course in each year
    for i in range(3):
        students_passed = students_passed * 1.5

    # Return the number of students who passed the course this year
    result = students_passed
    return result

print(solution())