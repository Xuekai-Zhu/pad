def solution():
    classes_in_pack = 10
    price_per_pack = 75
    price_per_added_class = (price_per_pack / classes_in_pack) * 1.33
    classes_added = 3
    total_classes = classes_in_pack + classes_added
    total_price = price_per_pack + (classes_added * price_per_added_class)
    result = total_price
    
    return result

print(solution())