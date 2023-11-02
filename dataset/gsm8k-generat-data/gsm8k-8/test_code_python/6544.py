def solution():
    # Calculate how much George had left after donating half of his income and spending $20 on groceries
    left_over = 100
    spent_on_groceries = 20
    donated_to_charity = left_over + spent_on_groceries

    # Calculate how much his monthly income was
    monthly_income = donated_to_charity * 4
    result = monthly_income
    return result

print(solution())