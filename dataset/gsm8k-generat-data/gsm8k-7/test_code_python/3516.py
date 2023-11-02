def solution():
    class_funds = 14
    total_contribution = 90
    num_students = 19

    # Reduce the total contribution by the class funds
    total_contribution -= class_funds

    # Divide the remaining amount equally among the students
    contribution_per_student = total_contribution / num_students
    result = contribution_per_student
    return result

print(solution())