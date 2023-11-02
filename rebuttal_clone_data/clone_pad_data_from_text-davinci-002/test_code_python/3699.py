def solution():
    carol_money = 60
    carol_save = 9
    mike_money = 90
    mike_save = 3
    weeks = 0
    while carol_money != mike_money:
        carol_money += carol_save
        mike_money += mike_save
        weeks += 1
    result = weeks
    return result

print(solution())