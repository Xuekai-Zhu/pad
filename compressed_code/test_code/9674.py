def solution():
    
    pocket_money = 450
    chocolates_spent = pocket_money * (1/9)
    fruits_spent = pocket_money * (2/5)
    money_left = pocket_money - chocolates_spent - fruits_spent
    result = money_left
    return result

print(solution())