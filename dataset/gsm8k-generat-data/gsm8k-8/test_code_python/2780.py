def solution():
    # Define the original prices
    cupcake_price = 3.00
    cookie_price = 2.00

    # Reduce the prices by half
    reduced_cupcake_price = 0.5 * cupcake_price
    reduced_cookie_price = 0.5 * cookie_price

    # Calculate the total revenue from selling the cupcakes and cookies
    total_revenue = (16 * reduced_cupcake_price) + (8 * reduced_cookie_price)

    result = total_revenue
    return result

print(solution())