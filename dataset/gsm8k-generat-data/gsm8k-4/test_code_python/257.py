def solution():
    """Hannah sold 40 pieces of cookies for $0.8 each and 30 cupcakes for $2 each. She used the money to buy 2 sets of measuring spoons for $6.5 each. How much money does she have left?"""
    # Calculate the total amount earned from selling cookies
    cookies_money = 40 * 0.8

    # Calculate the total amount earned from selling cupcakes
    cupcakes_money = 30 * 2

    # Calculate the total amount earned
    total_money = cookies_money + cupcakes_money

    # Calculate the cost of buying the measuring spoons
    measuring_spoons_cost = 2 * 6.5

    # Calculate the amount of money left
    money_left = total_money - measuring_spoons_cost

    # return the result
    result = money_left
    return result

print(solution())