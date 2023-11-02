def solution():
    salary_per_month = 60000 / 12  # Lee's salary per month
    savings_per_month = 1000  # Lee can save $1000 per month
    months_of_savings_needed = 2 * (salary_per_month / savings_per_month)  # Two months' salary needed for the ring
    result = months_of_savings_needed
    return result

print(solution())