def solution():
     jewelry_price = 30
     painting_price = 100
     jewelry_quantity = 2
     painting_quantity = 5
     new_jewelry_price = jewelry_price + 10
     new_painting_price = painting_price + 20
     total_price = (new_jewelry_price * jewelry_quantity) + (new_painting_price * painting_quantity)
     result = total_price
     return result

print(solution())