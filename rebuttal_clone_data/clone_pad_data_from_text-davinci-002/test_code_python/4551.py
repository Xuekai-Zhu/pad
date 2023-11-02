def solution():
    days_until_birthday = 22
    money_saved = 2
    cost_of_flower = 4
    total_money_saved = money_saved * days_until_birthday
    total_flowers = total_money_saved / cost_of_flower
    result = total_flowers
    return result

print(solution())