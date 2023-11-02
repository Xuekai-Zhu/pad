def solution():
    hours_per_day = 1  # John walks the dog for 1 hour per day
    rate_per_hour = 10 / (30 - 4)  # John is paid $10 for walking the dog 26 times in April
    total_wages = rate_per_hour * 26  # John earns a total of $260 in April

    total_expenses = 50 + 50  # John spends $50 on books and gives $50 to his sister
    remaining_money = total_wages - total_expenses
    result = remaining_money
    return result

print(solution())