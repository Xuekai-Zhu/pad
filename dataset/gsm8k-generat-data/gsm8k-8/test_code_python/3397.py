def solution():
    total_money = 48
    ryan_share = (2/3) * total_money
    leo_share = total_money - ryan_share
    leo_share += 10
    ryan_share -= 10
    leo_share -= 7
    ryan_share += 7
    leo_money = leo_share
    return leo_money

print(solution())