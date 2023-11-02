def solution():
     original_ice_cream_price = 12
     sale_ice_cream_price = original_ice_cream_price - 2
     price_per_can = 2
     cans_bought = 10
     total_price = (sale_ice_cream_price * 2) + (price_per_can * cans_bought)
     result = total_price
     return result

print(solution())