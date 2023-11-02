def solution():
    """The price of a home is $98 per square foot (sq ft). The house is 2,400 sq ft and the barn out back is 1,000 sq ft. How much is this property?"""
    house_sqft = 2400
    barn_sqft = 1000
    price_per_sqft = 98
    total_price = (house_sqft + barn_sqft) * price_per_sqft
    result = total_price
    return result

print(solution())