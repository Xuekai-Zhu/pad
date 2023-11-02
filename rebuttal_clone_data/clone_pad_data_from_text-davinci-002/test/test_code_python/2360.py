def solution():
    price_cucumbers = 5
    discount_tomatoes = 20
    price_two_kilos_tomatoes = ((100 - discount_tomatoes) / 100) * 2 * price_cucumbers
    price_three_kilos_cucumbers = 3 * price_cucumbers
    total_price = price_two_kilos_tomatoes + price_three_kilos_cucumbers
    result = total_price
    
    return result

print(solution())