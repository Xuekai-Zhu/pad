def solution():
    # Calculate Fred's salary 5 months ago
    fred_salary_5months_ago = 1000

    # Calculate Mike's salary 5 months ago
    mike_salary_5months_ago = 10 * fred_salary_5months_ago

    # Calculate Mike's salary now
    mike_salary_now = mike_salary_5months_ago * 1.4

    result = mike_salary_now
    return result

print(solution())