def solution():
    """Five months ago, Mike earned 10 times more money than Fred. If his salary has increased by 40 percent now, and Fred's salary then was $1000, calculate Mike's salary now."""
    # Define Fred's salary
    fred_salary = 1000

    # Calculate Mike's salary from five months ago
    mike_salary_5_months_ago = fred_salary * 10

    # Calculate Mike's current salary
    mike_salary_now = mike_salary_5_months_ago * 1.4

    result = mike_salary_now
    return result

print(solution())