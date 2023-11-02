def solution():
    initial_price = 1950
    price_decrease_per_year = 35
    num_years = 8  # from 2001 to 2009

    # Calculate the total decrease in price over 8 years
    total_price_decrease = price_decrease_per_year * num_years

    # Calculate the final price in 2009
    final_price = initial_price - total_price_decrease
    result = final_price
    return result

print(solution())