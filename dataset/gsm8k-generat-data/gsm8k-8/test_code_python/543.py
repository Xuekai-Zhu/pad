def solution():
    # Define the number of students and the cost per student
    total_students = 25
    cost_per_student = 50

    # Calculate the total amount paid by students who paid the full amount
    full_pay_students = total_students - 4
    full_pay_total = full_pay_students * cost_per_student

    # Calculate the total amount paid by students who paid half
    half_pay_total = 4 * (cost_per_student / 2)

    # Calculate the total amount gathered by the class
    total_gathered = full_pay_total + half_pay_total
    result = total_gathered
    return result

print(solution())