def solution():
    # Define the initial salary and the percent increase
    salary = 1000
    percent_increase = 0.1

    # Calculate the new salary after the raise
    new_salary = salary * (1 + percent_increase)

    # Calculate the total earnings for two months
    total_earnings = salary + new_salary
    result = total_earnings
    return result

print(solution())