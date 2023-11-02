def solution():
    # Define the original price and discount percentage
    original_price_per_kg = 5
    discount_percent = 40

    # Calculate the discounted price per kilogram
    discounted_price_per_kg = original_price_per_kg * (100 - discount_percent) / 100

    # Calculate the total cost for 10 kilograms
    total_cost = discounted_price_per_kg * 10
    result = total_cost
    return result

print(solution())