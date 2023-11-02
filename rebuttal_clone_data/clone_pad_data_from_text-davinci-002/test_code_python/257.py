def solution():
    """Hannah sold 40 pieces of cookies for $0.8 each and 30 cupcakes for $2 each. She used the money to buy 2 sets of measuring spoons for $6.5 each. How much money does she have left?"""
    cookie_sales = 40 * 0.8
    cupcake_sales = 30 * 2
    measuring_spoons = 2 * 6.5
    total_sales = cookie_sales + cupcake_sales - measuring_spoons
    result = total_sales
    return result

print(solution())