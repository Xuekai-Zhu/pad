def solution():
    """Monica is a teacher. She has 6 classes per day. The first class has 20 students. The second and third classes have 25 students. Her fourth class has half as many as her first class. Her fifth and sixth classes have 28 students. How many students does Monica see each day?"""
    # Define the number of students in each class
    class1_students = 20
    class2_students = 25
    class3_students = 25
    class4_students = class1_students / 2
    class5_students = 28
    class6_students = 28

    # Calculate the total number of students
    total_students = class1_students + class2_students + class3_students + class4_students + class5_students + class6_students

    # Return the result
    result = total_students
    return result

print(solution())