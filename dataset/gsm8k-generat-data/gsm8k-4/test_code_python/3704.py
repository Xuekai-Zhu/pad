def solution():
    """On Black Friday a popular electronics store sells 327 televisions. This is 50 more than they sold last Black Friday. If this sales trend continues and they sell 50 more televisions each year for three years, how many televisions will they sell on Black Friday three years from now?"""
    # Define the initial number of televisions sold
    tvs_sold = 327

    # Calculate the total number of televisions sold after 3 years
    for i in range(3):
        tvs_sold += 50

    # Display the number of televisions sold after 3 years
    result = tvs_sold
    return result

print(solution())