def solution():
     apples = 50
     oranges = 40
     price_apple = 0.80
     price_orange = 0.50
     apples_left = 10
     oranges_left = 6
     money_apple = apples_left * price_apple
     money_orange = oranges_left * price_orange
     total_money = money_apple + money_orange
     result = total_money
     return result

print(solution())