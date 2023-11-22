def solution():
    
    # Define the salary of Valerie and her brother
    VERIE_SALARY = 5000
    BROTHER_SALARY = VERIE_SALARY / 2

    # Calculate the combined salary of Valerie and her brother
    combined_salary = VERIE_SALARY + BROTHER_SALARY

    # Calculate the salary of their mother
    mother_salary = combined_salary * 2

    # Calculate the total salary they all have together
    total_salary = combined_salary + mother_salary

    # Display the total salary
    result = total_salary
    return result

print(solution())