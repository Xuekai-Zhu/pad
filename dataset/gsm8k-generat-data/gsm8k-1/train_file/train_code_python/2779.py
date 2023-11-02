def solution():
    """Crystal wanted to sell everything left in her pastry class before closing for the night. She reduced her $3.00 cupcakes and her $2.00 cookies by half. How much money did she make if she sold the last 16 cupcakes and 8 cookies?"""
    reduced_cupcake_price = 3 / 2
    reduced_cookie_price = 2 / 2
    total_cupcake_sales = reduced_cupcake_price * 16
    total_cookie_sales = reduced_cookie_price * 8
    total_sales = total_cupcake_sales + total_cookie_sales
    result = total_sales
    return result

print(solution())