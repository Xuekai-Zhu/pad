def solution():
    """In North Carolina, Jim bought 10 gallons of gas at $2.00/gallon. He paid $1.00 more per gallon in Virginia where he bought another 10 gallons of gas. How much has he spent on gas?"""
    nc_price = 2.00
    va_price = nc_price + 1.00
    nc_gallons = 10
    va_gallons = 10
    total_cost = (nc_gallons * nc_price) + (va_gallons * va_price)
    result = total_cost
    return result

print(solution())