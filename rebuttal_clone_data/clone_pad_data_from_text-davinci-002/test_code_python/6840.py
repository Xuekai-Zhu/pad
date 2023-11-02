def solution():
    Monday_spend = 80 / 2
    Tuesday_spend = Monday_spend / 5
    Wednesday_spend = Tuesday_spend * 3/8
    total_spend = Monday_spend + Tuesday_spend + Wednesday_spend
    money_left = 80 - total_spend
    result = money_left
    return result

print(solution())