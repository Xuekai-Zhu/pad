def solution():
    chocolate_flavored = 50
    mango_flavored = 54
    chocolate_sold = 3/5 * chocolate_flavored
    mango_sold = 2/3 * mango_flavored
    total_sold = chocolate_sold + mango_sold
    total_ice_creams = chocolate_flavored + mango_flavored
    result = total_ice_creams - total_sold
    
    return result

print(solution())