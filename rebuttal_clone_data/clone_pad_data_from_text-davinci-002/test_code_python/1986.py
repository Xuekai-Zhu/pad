def solution():
    money_total = 240
    samuel_share = money_total * 3/4
    samuel_spent = samuel_share * 1/5
    samuel_left = samuel_share - samuel_spent
    result = samuel_left
    return result

print(solution())