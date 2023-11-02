def solution():
    """Carol has $60 and saves $9 per week. Mike has $90 and saves $3 per week. How many weeks before Carol and Mike both have the same amount of money?"""
    carol_money = 60
    carol_savings_per_week = 9
    mike_money = 90
    mike_savings_per_week = 3
    weeks = 0
    while carol_money != mike_money:
        carol_money += carol_savings_per_week
        mike_money += mike_savings_per_week
        weeks += 1
    result = weeks
    return result

print(solution())