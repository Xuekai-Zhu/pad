def solution():
    """There are 325 students in a local high school. 40 percent of the students have glasses, how many students do not have glasses?"""
    # Define the total number of students
    total_students = 325

    # Calculate the number of students with glasses
    glasses_students = total_students * 0.4

    # Calculate the number of students without glasses
    noglasses_students = total_students - glasses_students

    # return the result
    result = noglasses_students
    return result

print(solution())