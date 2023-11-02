def solution():
    # Calculate the number of employees who got a salary or travel allowance increase
    employees_with_increase = 0.1 * 480 + 0.2 * 480  # 10% got a salary increase, 20% got a travel allowance increase
    employees_without_increase = 480 - employees_with_increase  # total employees minus those who received an increase
    result = employees_without_increase
    return result

print(solution())