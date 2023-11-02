def solution():
    """Hannah sold 40 pieces of cookies for $0.8 each and 30 cupcakes for $2 each.
    She used the money to buy 2 sets of measuring spoons for $6.5 each.
    How much money does she have left?"""
    # Calculate the total amount of money earned from selling cookies and cupcakes
    cookies = 40
    cookies_price = 0.8
    cupcakes = 30
    cupcakes_price = 2
    total_earned = (cookies * cookies_price) + (cupcakes * cupcakes_price)

    # Calculate the total cost of the measuring spoons
    measuring_spoons = 2
    measuring_spoons_cost = 6.5
    total_cost = measuring_spoons * measuring_spoons_cost

    # Calculate how much money Hannah has left
    money_left = total_earned - total_cost

    # Display the amount of money Hannah has left
    result = money_left
    return result

print(solution())