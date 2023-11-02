def solution():
     cows = 20
     pigs = cows * 4
     total_animals = cows + pigs
     pig_price = 400
     cow_price = 800
     total_price = pig_price * pigs + cow_price * cows
     result = total_price
     return result

print(solution())