def solution():
    """Five months ago, Mike earned 10 times more money than Fred. If his salary has increased by 40 percent now, and Fred's salary then was $1000, calculate Mike's salary now."""
    # Calculate how much Mike earned five months ago
    fred_salary = 1000
    mike_salary_5_months_ago = 10 * fred_salary

    # Calculate Mike's current salary
    mike_salary_now = mike_salary_5_months_ago * 1.4

    # Display Mike's current salary
    result = mike_salary_now
    return result

print(solution())