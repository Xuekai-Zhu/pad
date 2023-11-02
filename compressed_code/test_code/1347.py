def solution():
    
    tshirt_price = 5
    pants_price = 4
    skirt_price = 6
    refurbished_price = tshirt_price / 2
    total_income = (2*tshirt_price) + pants_price + (4*skirt_price) + (6*refurbished_price)
    result = total_income
    return result

print(solution())