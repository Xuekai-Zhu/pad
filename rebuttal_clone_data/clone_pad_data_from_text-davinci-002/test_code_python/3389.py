def solution():
     initial_price = 50
     percent_increase = 30
     percent_decrease = 20
     current_price = initial_price * (1 + percent_increase/100) * (1 - percent_decrease/100)
     result = current_price
     return result

print(solution())