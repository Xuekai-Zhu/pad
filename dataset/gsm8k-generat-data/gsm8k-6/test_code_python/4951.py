def solution():
    pocket_money = 450 # Joe's pocket money
    chocolates_spent = (1/9) * pocket_money # amount spent on chocolates
    fruits_spent = (2/5) * pocket_money # amount spent on fruits
    total_spent = chocolates_spent + fruits_spent # total amount spent
    money_left = pocket_money - total_spent # money left after spending on chocolates and fruits
    result = money_left
    return result

print(solution())