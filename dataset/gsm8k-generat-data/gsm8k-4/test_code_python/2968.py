def solution():
    """Jon makes 3/4's the salary that Karen makes. John makes $3000 per month. How long will it take him to make the same amount of money that Karen does in 3 months?"""
    # Define Jon's monthly salary and the fraction of Karen's salary he makes
    jon_salary = 3000
    karen_fraction = 3/4

    # Calculate Karen's monthly salary
    karen_salary = jon_salary / karen_fraction

    # Calculate the total amount Jon will make in 3 months
    jon_total = jon_salary * 3

    # Calculate the number of months it will take Jon to make the same amount as Karen in 3 months
    months = (karen_salary * 3) / jon_salary

    # Return the result
    result = months
    return result

print(solution())