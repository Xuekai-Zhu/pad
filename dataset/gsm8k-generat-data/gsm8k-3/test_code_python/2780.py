def solution():
    """Crystal wanted to sell everything left in her pastry class before closing for the night.  She reduced her $3.00 cupcakes and her $2.00 cookies by half.  How much money did she make if she sold the last 16 cupcakes and 8 cookies?"""
    # Define the original prices of the cupcakes and cookies
    CUPCAKE_PRICE = 3
    COOKIE_PRICE = 2

    # Calculate the new prices after reducing by half
    new_cupcake_price = CUPCAKE_PRICE / 2
    new_cookie_price = COOKIE_PRICE / 2

    # Calculate the total revenue from selling all the cupcakes and cookies
    total_revenue = (new_cupcake_price * 16) + (new_cookie_price * 8)

    # Display the total revenue
    result = total_revenue
    return result

print(solution())