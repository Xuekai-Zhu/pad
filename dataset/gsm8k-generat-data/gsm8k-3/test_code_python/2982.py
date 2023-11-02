def solution():
    """Harper needs to buy teacher appreciation gifts for her children’s teachers.  Her son has 3 different teachers and her daughter has 4.  If she spent $70 on gifts, how much did each gift cost?"""
    # Define the number of teachers
    num_teachers = 3 + 4

    # Define the total amount spent on gifts
    total_spent = 70

    # Calculate the cost per gift
    cost_per_gift = total_spent / num_teachers

    # Display the cost per gift
    result = cost_per_gift
    return result

print(solution())