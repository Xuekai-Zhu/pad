def solution():
    Patricia_money = 6
    Lisa_money = Patricia_money * 5
    Charlotte_money = Patricia_money / 2
    total_money = Patricia_money + Lisa_money + Charlotte_money
    money_needed = 100 - total_money
    result = money_needed
    return result

print(solution())