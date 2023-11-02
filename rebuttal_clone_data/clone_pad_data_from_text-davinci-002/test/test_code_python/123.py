def solution():
    
    initial_money = 100
    money_paid_to_colin = 20
    money_paid_to_helen = money_paid_to_colin * 2
    money_paid_to_benedict = money_paid_to_helen / 2
    total_money_paid = money_paid_to_colin + money_paid_to_helen + money_paid_to_benedict
    money_left = initial_money - total_money_paid
    result = money_left
    
    return result

print(solution())