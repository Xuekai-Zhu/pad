def solution():
    nc_price_per_gallon = 2.0
    va_price_per_gallon = nc_price_per_gallon + 1.0  # $1.00 more per gallon

    nc_gallons = 10
    va_gallons = 10

    # Calculate the total cost in North Carolina
    nc_total_cost = nc_gallons * nc_price_per_gallon

    # Calculate the total cost in Virginia
    va_total_cost = va_gallons * va_price_per_gallon

    # Calculate the total cost for all gas purchased
    total_cost = nc_total_cost + va_total_cost
    result = total_cost
    return result

print(solution())