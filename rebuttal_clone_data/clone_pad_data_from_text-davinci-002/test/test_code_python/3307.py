def solution():
    money = 50
    moses_percent = 40
    moses_money = money * (moses_percent / 100)
    tony_and_esther_money = money - moses_money
    tony_and_esther_money_each = tony_and_esther_money / 2
    moses_money_more = moses_money - tony_and_esther_money_each
    result = moses_money_more
    return result

print(solution())