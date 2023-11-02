def solution():
    sally_salary = 6  # Sally makes $6 per day as a babysitter
    bob_salary = 4  # Bob makes $4 per day as a babysitter
    days_in_a_year = 365  # There are 365 days in a year

    # Calculate Sally's savings
    sally_savings = (sally_salary * days_in_a_year) / 2

    # Calculate Bob's savings
    bob_savings = (bob_salary * days_in_a_year) / 2

    # Calculate the total savings
    total_savings = sally_savings + bob_savings
    result = total_savings
    return result

print(solution())