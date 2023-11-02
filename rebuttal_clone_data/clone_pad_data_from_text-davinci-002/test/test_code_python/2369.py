def solution():
     computer_price = 3000
     accessories_price = computer_price * 0.1
     total_price = computer_price + accessories_price
     initial_money = computer_price * 2
     money_left = initial_money - total_price
     result = money_left
     return result

print(solution())