def solution():
    
    tshirt_price = 5
    pants_price = 4
    skirt_price = 6
    refurbished_tshirt_price = tshirt_price / 2
    
    tshirt_quantity = 2
    pants_quantity = 1
    skirt_quantity = 4
    refurbished_tshirt_quantity = 6
    
    total_income = (tshirt_price * tshirt_quantity) + (pants_price * pants_quantity) + (skirt_price * skirt_quantity) + (refurbished_tshirt_price * refurbished_tshirt_quantity)
    
    result = total_income
    return result

print(solution())