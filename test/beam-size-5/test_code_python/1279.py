def solution():
    num_cupcakes = 20
    cupcake_price = 2

    num_cookies = 40
    cookie_price = 1

    num_trays = 5
    tray_price = 4

    # Calculate the total revenue from selling cupcakes
    cupcake_revenue = num_cupcakes * cupcake_price

    # Calculate the total revenue from selling cookies
    cookie_revenue = num_cookies * cookie_price

    # Calculate the total revenue from buying trays
    tray_revenue = num_trays * tray_price

    # Calculate the total revenue from all items
    total_revenue = cupcake_revenue + cookie_revenue

    # Calculate the amount of money Frances has left
    money_left = total_revenue - total_revenue
    result = money_left
    return result

print(solution())