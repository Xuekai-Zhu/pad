def solution():
    # Calculate the average price per class in the pack
    pack_price_per_class = 75 / 10

    # Calculate the price per additional class
    additional_class_price = pack_price_per_class * (1 + 1/3)

    # Calculate the total price for 13 classes
    total_price = (10 * pack_price_per_class) + (3 * additional_class_price)

    result = total_price
    return result

print(solution())