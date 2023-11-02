def solution():
    remaining_money = 100  # George has $100 left after donating and spending on groceries
    money_spent_on_groceries = 20  # George spent $20 on groceries
    money_donated = remaining_money + money_spent_on_groceries  # George donated half of his monthly income
    monthly_income = 2 * money_donated  # Monthly income = 2 * (money donated + money spent on groceries)
    result = monthly_income
    return result

print(solution())