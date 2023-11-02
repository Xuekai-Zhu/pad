def solution():
    
    chocolate_ice_creams = 50
    mango_ice_creams = 54
    chocolate_sold = int(chocolate_ice_creams * 3/5)
    mango_sold = int(mango_ice_creams * 2/3)
    total_sold = chocolate_sold + mango_sold
    total_not_sold = chocolate_ice_creams + mango_ice_creams - total_sold
    result = total_not_sold
    return result

print(solution())