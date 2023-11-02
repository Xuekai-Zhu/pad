def solution():
    carol_money = 60
    carol_saves_per_week = 9
    mike_money = 90
    mike_saves_per_week = 3

    weeks = 0

    # Keep adding savings to each person's money until they have the same amount
    while carol_money != mike_money:
        carol_money += carol_saves_per_week
        mike_money += mike_saves_per_week
        weeks += 1

    result = weeks
    return result

print(solution())