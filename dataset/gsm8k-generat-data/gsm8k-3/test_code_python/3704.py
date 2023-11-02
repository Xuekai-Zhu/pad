def solution():
    """On Black Friday a popular electronics store sells 327 televisions. This is 50 more than they sold last Black Friday. If this sales trend continues and they sell 50 more televisions each year for three years, how many televisions will they sell on Black Friday three years from now?"""
    # Define the number of televisions sold on the current Black Friday and the annual increase
    current_sales = 327
    annual_increase = 50

    # Calculate the sales for the next three Black Fridays
    sales_year_2 = current_sales + annual_increase
    sales_year_3 = sales_year_2 + annual_increase
    sales_year_4 = sales_year_3 + annual_increase

    # Display the sales on the third Black Friday from now
    result = sales_year_4
    return result

print(solution())