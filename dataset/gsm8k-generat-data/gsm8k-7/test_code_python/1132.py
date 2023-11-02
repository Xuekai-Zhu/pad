def solution():
    original_employees = 852
    percent_increase = 0.25  # 25% increase

    # Calculate the number of new employees that were hired
    new_employees = original_employees * percent_increase

    # Calculate the total number of employees now in the factory
    total_employees = original_employees + new_employees
    result = total_employees
    return result

print(solution())