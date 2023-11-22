def solution():
    
    # Define the total amount raised
    total_raised = 175000

    # Define the amount raised from organizations
    organization_raised = 50000

    # Calculate the amount raised from students
    student_raised = total_raised - organization_raised

    # Calculate the amount raised by each student
    student_raised_per_student = student_raised / 20

    # Display the amount raised by each student
    result = student_raised_per_student
    return result

print(solution())