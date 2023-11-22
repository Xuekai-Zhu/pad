def solution():
    
    # Define the prices and quantities of cupcakes and cookies
    cupcake_price = 2
    cookie_price = 1
    cupcake_qty = 20
    cookie_qty = 40

    # Calculate the total revenue from cupcakes and cookies
    cupcake_revenue = cupcake_price * cupcake_qty
    cookie_revenue = cookie_price * cookie_qty
    total_revenue = cupcake_revenue + cookie_revenue

    # Calculate the total cost of the trays
    tray_cost = 4 * 5

    # Calculate the total cost of all items
    total_cost = total_revenue + tray_cost

    # Calculate the money left after buying the trays
    money_left = total_cost - total_cost

    # return the result
    result = money_left
    return result

print(solution())