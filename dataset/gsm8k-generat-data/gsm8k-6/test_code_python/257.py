def solution():
    # Calculate the total amount of money Hannah earned
    cookies_price = 0.8
    cupcakes_price = 2
    cookies_sold = 40
    cupcakes_sold = 30
    
    total_earned = cookies_price * cookies_sold + cupcakes_price * cupcakes_sold

    # Calculate the total amount of money spent on measuring spoons
    measuring_spoons_price = 6.5
    measuring_spoons_sets = 2

    total_spent = measuring_spoons_price * measuring_spoons_sets

    # Calculate the amount of money Hannah has left
    money_left = total_earned - total_spent
    result = money_left
    return result

print(solution())