def solution():
    original_employees = 852  # The factory originally employed 852 people

    # Calculate the number of additional employees hired (25% more than the original amount)
    additional_employees = original_employees * 0.25

    # Calculate the new total number of employees
    total_employees = original_employees + additional_employees
    result = total_employees
    return result

print(solution())