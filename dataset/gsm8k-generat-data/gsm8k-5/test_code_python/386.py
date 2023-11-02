def solution():
    # Calculate the discount for shoes
    discount_shoes = 0.4  # 40 percent off on shoes
    price_shoes = 50  # Original price for a pair of shoes
    num_shoes = 2  # Daniela buys 2 pairs of shoes
    total_price_shoes = price_shoes * num_shoes
    total_discount_shoes = total_price_shoes * discount_shoes

    # Calculate the discount for the dress
    discount_dress = 0.2  # 20 percent off on the dress
    price_dress = 100
    total_discount_dress = price_dress * discount_dress

    # Calculate the final amount Daniela spends
    final_price = (total_price_shoes - total_discount_shoes) + (price_dress - total_discount_dress)
    result = final_price
    return result

print(solution())