def solution():
    """On Black Friday a popular electronics store sells 327 televisions. This is 50 more than they sold last Black Friday. If this sales trend continues and they sell 50 more televisions each year for three years, how many televisions will they sell on Black Friday three years from now?"""
    starting_sales = 327
    annual_increase = 50
    num_years = 3
    total_increase = annual_increase * num_years
    future_sales = starting_sales + total_increase
    result = future_sales
    return result

print(solution())