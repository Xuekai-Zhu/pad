def solution():
    # Calculate the total amount of money Daria will have after saving for certain weeks
    weeks = 0
    total_money = 20
    while total_money < 120:
        total_money += 10
        weeks += 1

    result = weeks
    return result

print(solution())