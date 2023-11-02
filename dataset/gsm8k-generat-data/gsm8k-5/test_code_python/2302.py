def solution():
    price_2001 = 1950  # Price in 2001 is known
    years_passed = 8  # We need to find the price in 2009, 8 years later
    price_decrease_per_year = 35  # The price decreases by $35 each year

    # Calculate the price in 2009
    price_2009 = price_2001 - (years_passed * price_decrease_per_year)
    result = price_2009
    return result

print(solution())