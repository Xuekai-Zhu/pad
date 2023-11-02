def solution():
    fred_salary = 1000
    mike_salary_five_months_ago = fred_salary * 10

    # Calculate Mike's salary now with the 40% increase
    mike_salary_now = mike_salary_five_months_ago * 1.4
    result = mike_salary_now
    return result

print(solution())