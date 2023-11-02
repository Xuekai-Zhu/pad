def solution():
    pocket_money = 450
    spent_on_chocolates = pocket_money / 9
    spent_on_fruits = pocket_money * 2/5
    money_left = pocket_money - spent_on_chocolates - spent_on_fruits
    result = money_left
    return result

print(solution())