def solution():
     nights = 3
     cats = 2
     dogs = 3
     price_per_animal = 13
     total_price = nights * (cats + dogs) * price_per_animal
     result = total_price
     return result

print(solution())