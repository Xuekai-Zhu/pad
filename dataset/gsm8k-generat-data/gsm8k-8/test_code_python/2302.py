def solution():
    # Define the initial price and the number of years between 2001 and 2009
    initial_price = 1950
    num_years = 8

    # Calculate the total price decrease over the 8 years
    total_decrease = num_years * 35

    # Calculate the final price in 2009
    final_price = initial_price - total_decrease
    result = final_price
    return result

print(solution())