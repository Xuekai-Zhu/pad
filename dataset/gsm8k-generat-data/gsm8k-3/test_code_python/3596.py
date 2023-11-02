def solution():
    """Two-thirds of the class have brown eyes. Half of the students with brown eyes have black hair. If there are 6 students in the class with brown eyes and black hair, how many students are there in total?"""

    # Calculate the total number of students with brown eyes
    total_brown_eyes = 6 / (1/2)   # 6 students with black hair is half of the total students with brown eyes

    # Calculate the total number of students in the class
    total_students = total_brown_eyes / (2/3)   # Two-thirds of the class have brown eyes

    # Display the total number of students in the class
    result = total_students
    return result

print(solution())