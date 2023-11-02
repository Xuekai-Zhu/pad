def solution():
    cucumber_price_per_kilo = 5.0
    tomato_price_per_kilo = cucumber_price_per_kilo * 0.8  # 20% cheaper

    # Calculate the total cost of two kilograms of tomatoes
    total_tomato_cost = tomato_price_per_kilo * 2

    # Calculate the total cost of three kilograms of cucumbers
    total_cucumber_cost = cucumber_price_per_kilo * 3

    # Calculate the total cost of all vegetables
    total_cost = total_tomato_cost + total_cucumber_cost
    result = total_cost
    return result

print(solution())