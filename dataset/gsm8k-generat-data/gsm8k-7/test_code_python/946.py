def solution():
    pack_price = 75
    pack_classes = 10
    additional_price_ratio = 1/3
    total_classes = 13

    # Calculate the average price per class in the pack
    pack_price_per_class = pack_price / pack_classes

    # Calculate the price per class for additional classes
    additional_price_per_class = pack_price_per_class * (1 + additional_price_ratio)

    # Calculate the total cost of all classes
    total_cost = pack_price + (additional_price_per_class * (total_classes - pack_classes))
    result = total_cost
    return result

print(solution())