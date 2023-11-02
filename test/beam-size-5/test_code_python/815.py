def solution():
    num_students = 20
    total_raised = 175000
    organizations_raised = 50000

    # Calculate the total amount raised from non-organizations
    non_organizations_raised = total_raised - organizations_raised

    # Calculate the amount raised per student
    amount_per_student = non_organizations_raised / num_students
    result = amount_per_student
    return result

print(solution())