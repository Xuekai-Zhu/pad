def solution():
     pineapples_bought = 6
     pineapple_price = 3
     pineapple_rings = 12
     rings_sold = 4
     sale_price = 5
     cost = pineapples_bought * pineapple_price
     income = rings_sold * sale_price
     profit = income - cost
     result = profit
     return result

print(solution())