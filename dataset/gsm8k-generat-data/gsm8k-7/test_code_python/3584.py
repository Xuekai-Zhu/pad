def solution():
    monthly_income = 20 + 40  # $20 for washing cars and $40 for walking dogs
    savings_per_month = monthly_income / 2  # Mary saves half her monthly income
    savings_goal = 150
    num_months = savings_goal / savings_per_month
    result = num_months
    return result

print(solution())