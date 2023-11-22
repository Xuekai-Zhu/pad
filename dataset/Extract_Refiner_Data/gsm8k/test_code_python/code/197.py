def solution():
    
    # Define the initial salary and the percentage increase
    INITIAL_SALARY = 5000
    PERCENT_INCREASE = 0.05

    # Calculate the new salary after the increase
    new_salary = INITIAL_SALARY * (1 + PERCENT_INCREASE)

    # Calculate the total salary over the year
    total_salary = new_salary * 2000

    # Calculate the total money John made over the year
    total_money = total_salary * 52

    # Display the total money John made
    result = total_money
    return result

print(solution())