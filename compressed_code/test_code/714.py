def solution():
    
    pack_price = 75
    pack_classes = 10
    additional_class_price = (4/3) * (pack_price / pack_classes)
    total_classes = 13
    additional_classes = total_classes - pack_classes
    total_price = pack_price + (additional_classes * additional_class_price)
    result = total_price
    return result

print(solution())