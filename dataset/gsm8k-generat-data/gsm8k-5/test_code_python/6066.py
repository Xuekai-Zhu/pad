def solution():
    # Calculate the price of one CD by "The Dark"
    the_dark_price = 2 * 12  # "AVN" CD costs $12, which is half the price of one CD by "The Dark"
    one_the_dark_price = the_dark_price / 2  

    # Calculate the total cost of all CDs by "The Dark"
    total_the_dark_price = 2 * one_the_dark_price  

    # Calculate the cost of all 90s music CDs
    total_90s_cds_price = 0.4 * (total_the_dark_price + 12)  

    # Calculate the total cost of all CDs Alan is going to buy
    total_price = total_the_dark_price + 12 + total_90s_cds_price  

    result = total_price
    return result

print(solution())