def solution():
    carol_money = 60  # initial amount of money Carol has
    mike_money = 90   # initial amount of money Mike has
    weeks = 0         # number of weeks it takes for Carol and Mike to have the same amount of money

    while carol_money != mike_money:
        carol_money += 9    # Carol saves $9 per week
        mike_money += 3     # Mike saves $3 per week
        weeks += 1

    return weeks

print(solution())