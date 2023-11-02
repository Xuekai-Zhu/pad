def solution():
    """The teacher brings in 14 mini-cupcakes and 12 donut holes for the class. There are 13 students in the class. If each student gets the exact same amount, how many desserts does each student get?"""
    # Calculate the total number of desserts
    total_desserts = 14 + 12

    # Calculate the number of desserts each student gets
    dessert_per_student = total_desserts // 13

    # Display the number of desserts each student gets
    result = dessert_per_student
    return result

print(solution())