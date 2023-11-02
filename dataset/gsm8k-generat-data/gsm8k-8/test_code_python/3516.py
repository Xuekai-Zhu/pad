def solution():
    # Define the total contribution needed per class
    total_contribution = 90

    # Get the remaining class funds
    class_funds = 14

    # Subtract the class funds from the total contribution
    remaining_contribution = total_contribution - class_funds

    # Divide the remaining contribution among the number of students
    num_students = 19
    contribution_per_student = remaining_contribution / num_students

    result = contribution_per_student
    return result

print(solution())