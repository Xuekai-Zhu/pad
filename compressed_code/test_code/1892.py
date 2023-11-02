def solution():
    
    bea_price = 25
    dawn_price = 28
    bea_glasses_sold = 10
    dawn_glasses_sold = 8
    bea_earnings = bea_price * bea_glasses_sold
    dawn_earnings = dawn_price * dawn_glasses_sold
    difference = bea_earnings - dawn_earnings
    result = difference
    return result

print(solution())