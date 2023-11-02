def solution():
    num_cookies = 40
    cookie_price = 0.8
    num_cupcakes = 30
    cupcake_price = 2
    num_spoons_sets = 2
    spoons_set_price = 6.5

    # Calculate the total amount of money Hannah received from selling cookies
    cookies_sale = num_cookies * cookie_price

    # Calculate the total amount of money Hannah received from selling cupcakes
    cupcakes_sale = num_cupcakes * cupcake_price

    # Calculate the total amount of money Hannah spent on measuring spoons
    spoons_cost = num_spoons_sets * spoons_set_price

    # Calculate the total amount of money Hannah has left
    total_left = cookies_sale + cupcakes_sale - spoons_cost
    result = total_left
    return result

print(solution())