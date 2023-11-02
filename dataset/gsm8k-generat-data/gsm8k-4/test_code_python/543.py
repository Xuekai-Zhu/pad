def solution():
    """In Mary's class, there are 25 students. Their teacher told them they could pay $50 each to finance a big science project that they and their society would benefit greatly from. They all paid the full amount except for 4 students, who paid half. How much was the class able to gather together?"""
    # Define the total number of students and the cost per student
    total_students = 25
    cost_per_student = 50

    # Calculate the total amount collected from the students who paid full amount
    full_amount_total = (total_students - 4) * cost_per_student

    # Calculate the total amount collected from the students who paid half amount
    half_amount_total = 4 * (cost_per_student / 2)

    # Calculate the total amount collected from the class
    total_amount = full_amount_total + half_amount_total

    result = total_amount
    return result

print(solution())