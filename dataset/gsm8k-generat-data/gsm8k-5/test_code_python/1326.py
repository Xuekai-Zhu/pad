def solution():
    # Calculate the total amount Gargamel spent on the sale price
    total_sale_price = 4 * 75  # Gargamel bought 4 tires on sale for $75 each
    total_original_price = total_sale_price + 36  # Gargamel saved a total of $36 on the tires

    # Calculate the original price of each tire
    original_price_per_tire = total_original_price / 4
    result = original_price_per_tire
    return result

print(solution())