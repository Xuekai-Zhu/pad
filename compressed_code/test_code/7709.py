def solution():
    
    bea_price = 25
    dawn_price = 28
    bea_sales = 10
    dawn_sales = 8
    bea_earnings = bea_price * bea_sales
    dawn_earnings = dawn_price * dawn_sales
    diff_earnings = bea_earnings - dawn_earnings
    result = diff_earnings
    return result

print(solution())