def solution():
    """The teacher brings in 14 mini-cupcakes and 12 donut holes for the class. There are 13 students in the class. If each student gets the exact same amount, how many desserts does each student get?"""
    # Define the total number of desserts
    total_desserts = 14 + 12

    # Define the number of students in the class
    num_students = 13

    # Calculate the number of desserts per student
    desserts_per_student = total_desserts // num_students

    # Return the result
    result = desserts_per_student
    return result

print(solution())