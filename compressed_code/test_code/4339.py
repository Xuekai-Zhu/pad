def solution():
    
    apple_price_per_kg = 5
    discount = 0.4
    discounted_price_per_kg = apple_price_per_kg - (apple_price_per_kg * discount)
    total_price = discounted_price_per_kg * 10
    result = total_price
    return result

print(solution())