def solution():
    """In North Carolina, Jim bought 10 gallons of gas at $2.00/gallon. He paid $1.00 more per gallon in Virginia where he bought another 10 gallons of gas. How much has he spent on gas?"""
    nc_price_per_gallon = 2.00
    va_price_per_gallon = nc_price_per_gallon + 1.00
    total_gallons = 20
    total_spent = (nc_price_per_gallon * 10) + (va_price_per_gallon * 10)
    result = total_spent
    return result

print(solution())