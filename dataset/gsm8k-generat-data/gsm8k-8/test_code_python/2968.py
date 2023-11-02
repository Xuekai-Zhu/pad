def solution():
    # Define the fraction of Karen's salary that Jon makes
    jon_to_karen_fraction = 3/4

    # Calculate Karen's monthly salary
    karen_monthly_salary = 3000 / jon_to_karen_fraction

    # Calculate the total amount Karen makes in 3 months
    karen_total_salary = karen_monthly_salary * 3

    # Calculate how long it will take Jon to make the same amount
    jon_salary_per_month = 3000
    months_to_match_salary = karen_total_salary / jon_salary_per_month

    result = months_to_match_salary
    return result

print(solution())