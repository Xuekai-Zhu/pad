def solution():
    # Calculate the number of years from 2001 to 2009
    years = 2009 - 2001

    # Calculate the total decrease in price over the years
    total_decrease = years * 35

    # Calculate the price of the TV in 2009
    price_2009 = 1950 - total_decrease
    result = price_2009
    return result

print(solution())