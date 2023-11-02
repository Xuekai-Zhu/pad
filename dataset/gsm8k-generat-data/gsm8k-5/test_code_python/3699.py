def solution():
    carol_money = 60
    mike_money = 90
    carol_savings_per_week = 9
    mike_savings_per_week = 3
    weeks = 0

    while carol_money != mike_money:
        carol_money += carol_savings_per_week
        mike_money += mike_savings_per_week
        weeks += 1

    result = weeks
    return result

print(solution())