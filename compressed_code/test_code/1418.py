def solution():
    
    foster_chickens = 45
    summit_water = foster_chickens * 2
    hormel_chickens = foster_chickens * 3
    boudin_chickens = hormel_chickens // 3
    delmonte_water = summit_water - 30
    total_items = foster_chickens + summit_water + hormel_chickens + boudin_chickens + delmonte_water
    result = total_items
    return result

print(solution())