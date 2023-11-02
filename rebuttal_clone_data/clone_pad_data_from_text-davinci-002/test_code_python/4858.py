def solution():
     increased_price_lemon = 4
     increased_price_grape = increased_price_lemon / 2
     new_price_lemon = 8 + increased_price_lemon
     new_price_grape = 7 + increased_price_grape
     lemon_quantity = 80
     grape_quantity = 140
     total_price = (new_price_lemon * lemon_quantity) + (new_price_grape * grape_quantity)
     result = total_price
     return result

print(solution())