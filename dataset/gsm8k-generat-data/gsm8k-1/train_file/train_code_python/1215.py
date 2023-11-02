def solution():
    """The teacher brings in 14 mini-cupcakes and 12 donut holes for the class. There are 13 students in the class. If each student gets the exact same amount, how many desserts does each student get?"""
    total_desserts = 14 + 12
    num_students = 13
    desserts_per_student = total_desserts / num_students
    result = desserts_per_student
    return result

print(solution())