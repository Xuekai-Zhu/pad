def solution():
    """The price of a home is $98 per square foot (sq ft). The house is 2,400 sq ft and the barn out back is 1,000 sq ft. How much is this property?"""
    price_per_sq_ft = 98
    house_sq_ft = 2400
    barn_sq_ft = 1000
    total_sq_ft = house_sq_ft + barn_sq_ft
    property_price = total_sq_ft * price_per_sq_ft
    result = property_price
    return result

print(solution())