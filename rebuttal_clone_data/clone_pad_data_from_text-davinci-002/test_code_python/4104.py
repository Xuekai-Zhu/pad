def solution():
     candy_price = 0.1
     classmates = 35
     candies_bought = classmates * 2
     candies_left = 12
     candies_eaten = candies_bought - candies_left
     money_spent = candy_price * candies_eaten
     result = money_spent
     return result

print(solution())