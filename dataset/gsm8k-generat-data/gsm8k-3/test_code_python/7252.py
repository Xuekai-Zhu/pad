def solution():
    """In North Carolina, Jim bought 10 gallons of gas at $2.00/gallon.  He paid $1.00 more per gallon in Virginia where he bought another 10 gallons of gas.  How much has he spent on gas?"""
    # Define the number of gallons purchased and the cost per gallon in each state
    NC_GALLONS = 10
    NC_PRICE = 2
    VA_GALLONS = 10
    VA_PRICE = NC_PRICE + 1

    # Calculate the total cost of gas in North Carolina
    nc_cost = NC_GALLONS * NC_PRICE

    # Calculate the total cost of gas in Virginia
    va_cost = VA_GALLONS * VA_PRICE

    # Calculate the total cost of gas for the entire trip
    total_cost = nc_cost + va_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())