def solution():
    """On Black Friday a popular electronics store sells 327 televisions. This is 50 more than they sold last Black Friday. 
    If this sales trend continues and they sell 50 more televisions each year for three years, 
    how many televisions will they sell on Black Friday three years from now?"""
    current_sales = 327
    sales_increase = 50
    total_sales = current_sales + (sales_increase * 3)
    result = total_sales
    return result

print(solution())