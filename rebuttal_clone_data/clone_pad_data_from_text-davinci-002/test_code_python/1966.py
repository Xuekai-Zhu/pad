def solution():
    pants = 3
    shorts = 5
    shirts_bought = 2
    money = 30
    
    money_from_pants = pants * 5
    money_from_shorts = shorts * 3
    money_spent_on_shirts = shirts_bought * 10
    
    money_left = money - (money_from_pants + money_from_shorts + money_spent_on_shirts)
    shirts_sold = money_left / 4
    
    result = shirts_sold
    return result

print(solution())