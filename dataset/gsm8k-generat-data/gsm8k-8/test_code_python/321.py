def solution():
    # Calculate Fred's salary 5 months ago
    fred_salary_five_months_ago = 1000

    # Calculate Mike's salary 5 months ago
    mike_salary_five_months_ago = 10 * fred_salary_five_months_ago

    # Calculate Mike's current salary
    mike_current_salary = mike_salary_five_months_ago * 1.4

    result = mike_current_salary
    return result

print(solution())