def solution():
    # Calculate the total amount paid by Gargamel for 4 tires on sale
    total_paid = 4 * 75  # Gargamel bought 4 tires on sale for $75 each

    # Calculate the total amount he would have paid if the tires weren't on sale
    total_original_price = total_paid + 36  # Gargamel saved $36 in total

    # Calculate the original price of each tire
    original_price = total_original_price / 4
    result = original_price
    return result

print(solution())