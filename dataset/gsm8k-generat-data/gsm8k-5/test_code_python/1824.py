def solution():
    foster_chickens = 45
    summit_water = 2 * foster_chickens
    hormel_chickens = 3 * foster_chickens
    boudin_chickens = hormel_chickens / 3
    delmonte_water = summit_water - 30
    
    # Calculate the total number of food items donated
    total_items = foster_chickens + summit_water + hormel_chickens + boudin_chickens + delmonte_water
    result = total_items
    return result

print(solution())