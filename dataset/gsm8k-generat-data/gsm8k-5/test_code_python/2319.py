def solution():
    price_per_dog = 1000  # Mr. Mayer bought each Corgi dog for $1000
    profit_margin = 0.3  # Mr. Mayer plans to sell them with a 30% profit
    selling_price_per_dog = price_per_dog * (1 + profit_margin)  # Selling price per dog with the profit margin
    quantity = 2  # Mr. Mayer's friend wants to buy two dogs

    # Calculate the total price Mr. Mayer's friend should pay
    total_price = selling_price_per_dog * quantity
    result = total_price
    return result

print(solution())