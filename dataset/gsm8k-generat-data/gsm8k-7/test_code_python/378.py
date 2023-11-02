def solution():
    cupcakes = 20
    cupcake_price = 1.5

    cookies = 10
    cookie_price = 2

    biscuits = 20
    biscuit_price = 1

    days = 5

    # Calculate the total earnings from cupcakes
    total_cupcake_earnings = cupcakes * cupcake_price * days

    # Calculate the total earnings from cookies
    total_cookie_earnings = cookies * cookie_price * days

    # Calculate the total earnings from biscuits
    total_biscuit_earnings = biscuits * biscuit_price * days

    # Calculate the total earnings for all items
    total_earnings = total_cupcake_earnings + total_cookie_earnings + total_biscuit_earnings
    result = total_earnings
    return result

print(solution())