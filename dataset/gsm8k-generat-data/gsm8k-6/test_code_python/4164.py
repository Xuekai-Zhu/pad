def solution():
    # Calculate the price of one kilogram of tomatoes and the discount
    price_cucumbers = 5
    discount = 0.2
    price_tomatoes = price_cucumbers * (1 - discount)

    # Calculate the total cost of two kilograms of tomatoes and three kilograms of cucumbers
    total_cost = 2 * price_tomatoes + 3 * price_cucumbers
    result = total_cost
    return result

print(solution())