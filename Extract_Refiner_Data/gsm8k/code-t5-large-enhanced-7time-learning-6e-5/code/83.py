def solution():
    
    # Define the initial salary and the percentage increase for employees who stayed in the company for 5 years
    initial_salary = 600
    percentage_increase = 0.1

    # Calculate the annual salary after 5 years of service
    annual_salary = initial_salary * 12 * (1 + percentage_increase)

    # Calculate the annual salary after 3 years of service
    annual_salary += annual_salary * 3

    # Display the annual salary
    result = annual_salary
    return result

print(solution())