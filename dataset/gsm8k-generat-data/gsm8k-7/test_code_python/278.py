def solution():
    price_per_sqft = 98
    house_sqft = 2400
    barn_sqft = 1000

    # Calculate the total square footage of the property
    total_sqft = house_sqft + barn_sqft

    # Calculate the total price of the property
    total_price = total_sqft * price_per_sqft
    result = total_price
    return result

print(solution())