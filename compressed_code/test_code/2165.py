def solution():
    
    original_cupcake_price = 3.00
    original_cookie_price = 2.00
    reduced_cupcake_price = original_cupcake_price / 2
    reduced_cookie_price = original_cookie_price / 2
    total_money_made = (reduced_cupcake_price * 16) + (reduced_cookie_price * 8)
    result = total_money_made
    return result

print(solution())