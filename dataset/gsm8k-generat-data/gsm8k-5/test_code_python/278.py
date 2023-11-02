def solution():
    price_per_sq_ft = 98  # The price per square foot is $98
    house_area = 2400  # The house has an area of 2,400 sq ft
    barn_area = 1000  # The barn has an area of 1,000 sq ft

    # Calculate the total cost of the property
    total_cost = price_per_sq_ft * (house_area + barn_area)
    result = total_cost
    return result

print(solution())