def solution():
    pocket_money = 450
    chocolates_spent = pocket_money / 9
    fruits_spent = (2/5) * pocket_money

    total_spent = chocolates_spent + fruits_spent
    money_left = pocket_money - total_spent
    result = money_left
    return result

print(solution())