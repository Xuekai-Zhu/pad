def solution():
     cost_of_dog = 1000
     percent_profit = 30
     profit = cost_of_dog * (percent_profit / 100)
     sale_price = cost_of_dog + profit
     number_of_dogs = 2
     total_price = sale_price * number_of_dogs
     result = total_price
     return result

print(solution())