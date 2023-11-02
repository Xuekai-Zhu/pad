def solution():
    # Original prices of cupcakes and cookies
    cupcake_price = 3.00
    cookie_price = 2.00

    # Reduced prices after discount
    discounted_cupcake_price = cupcake_price / 2
    discounted_cookie_price = cookie_price / 2

    # Total amount earned from selling cupcakes and cookies
    total_amount = (discounted_cupcake_price * 16) + (discounted_cookie_price * 8)
    result = total_amount
    return result

print(solution())