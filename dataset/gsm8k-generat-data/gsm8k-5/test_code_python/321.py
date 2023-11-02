def solution():
    # Let x be Mike's salary 5 months ago
    # Then 10x was Fred's salary 5 months ago
    fred_salary = 1000
    x = 10 * fred_salary / 2

    # Calculate Mike's current salary
    current_salary = x * 1.4

    result = current_salary
    return result

print(solution())