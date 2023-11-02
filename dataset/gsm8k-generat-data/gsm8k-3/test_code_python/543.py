def solution():
    """In Mary's class, there are 25 students. Their teacher told them they could pay $50 each to finance a big science project that they and their society would benefit greatly from. They all paid the full amount except for 4 students, who paid half. How much was the class able to gather together?"""
    # Define the total number of students and the cost per student
    num_students = 25
    full_cost = 50

    # Calculate the total amount gathered from full-paying students
    full_paid = (num_students - 4) * full_cost

    # Calculate the total amount gathered from half-paying students
    half_paid = 4 * (full_cost / 2)

    # Calculate the total amount gathered by the class
    total_gathered = full_paid + half_paid

    # Display the total amount gathered
    result = total_gathered
    return result

print(solution())