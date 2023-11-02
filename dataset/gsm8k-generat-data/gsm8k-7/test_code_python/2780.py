def solution():
    original_cupcake_price = 3.0
    original_cookie_price = 2.0

    # Reduce cupcake price by half
    reduced_cupcake_price = original_cupcake_price / 2

    # Reduce cookie price by half
    reduced_cookie_price = original_cookie_price / 2

    num_cupcakes_sold = 16
    num_cookies_sold = 8

    # Calculate the total amount of money made from selling cupcakes
    total_cupcake_money = num_cupcakes_sold * reduced_cupcake_price

    # Calculate the total amount of money made from selling cookies
    total_cookie_money = num_cookies_sold * reduced_cookie_price

    # Calculate the total amount of money made from selling all pastry items
    total_money = total_cupcake_money + total_cookie_money
    result = total_money
    return result

print(solution())