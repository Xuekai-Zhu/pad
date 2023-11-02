def solution():
    """Monica is a teacher. She has 6 classes per day. The first class has 20 students. The second and third classes have 25 students. Her fourth class has half as many as her first class. Her fifth and sixth classes have 28 students. How many students does Monica see each day?"""
    # Define the number of students in each class
    class_1 = 20
    class_2 = 25
    class_3 = 25
    class_4 = class_1 / 2
    class_5 = 28
    class_6 = 28

    # Calculate the total number of students
    total_students = class_1 + class_2 + class_3 + class_4 + class_5 + class_6

    # Display the total number of students
    result = total_students
    return result

print(solution())