def solution():
    """Twenty students are working together to raise money for a charity. Each earns the same amount. The charity raises a total of $175,000. $50,000 comes from organizations and the rest from the students. How much did each student raise?"""
    total_raised = 175000
    org_donation = 50000
    students_raised = total_raised - org_donation
    num_students = 20
    amount_per_student = students_raised / num_students
    result = amount_per_student
    return result

print(solution())