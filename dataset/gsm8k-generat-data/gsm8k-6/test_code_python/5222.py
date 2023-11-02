def solution():
    # Calculate the equivalent price for 1 gallon of mayo in the normal store
    price_normal_store = (3/16) * 128  # 3 dollars for a 16-ounce bottle, 128 ounces in 1 gallon
    price_bulk = 8  # 1 gallon of mayo at Costco costs 8 dollars

    # Calculate the amount saved by buying in bulk
    amount_saved = price_normal_store - price_bulk
    result = amount_saved
    return result

print(solution())