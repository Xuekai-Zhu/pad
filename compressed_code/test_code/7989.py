def solution():
    
    reduced_cupcake_price = 3 / 2
    reduced_cookie_price = 2 / 2
    total_cupcake_sales = reduced_cupcake_price * 16
    total_cookie_sales = reduced_cookie_price * 8
    total_sales = total_cupcake_sales + total_cookie_sales
    result = total_sales
    return result

print(solution())