def solution():
    """Two-thirds of the class have brown eyes. Half of the students with brown eyes have black hair. If there are 6 students in the class with brown eyes and black hair, how many students are there in total?"""
    # Define the proportion of students with brown eyes and the number of students with brown eyes
    brown_eyes_proportion = 2/3
    brown_eyes_students = 6 / (1/2)

    # Calculate the total number of students
    total_students = brown_eyes_students / brown_eyes_proportion

    # return the result
    result = total_students
    return result

print(solution())