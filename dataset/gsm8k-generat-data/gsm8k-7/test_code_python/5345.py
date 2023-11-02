def solution():
    salary_per_month = 60000 / 12  # calculate monthly salary
    savings_per_month = 1000
    proposal_budget = salary_per_month * 2  # calculate proposal budget
    months_needed = proposal_budget / savings_per_month
    result = months_needed
    return result

print(solution())