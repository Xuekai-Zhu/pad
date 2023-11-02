def solution():
    """Crystal wanted to sell everything left in her pastry class before closing for the night. She reduced her $3.00 cupcakes and her $2.00 cookies by half. How much money did she make if she sold the last 16 cupcakes and 8 cookies?"""
    original_cupcake_price = 3.00
    original_cookie_price = 2.00
    reduced_cupcake_price = original_cupcake_price / 2
    reduced_cookie_price = original_cookie_price / 2
    total_money_made = (reduced_cupcake_price * 16) + (reduced_cookie_price * 8)
    result = total_money_made
    return result

print(solution())