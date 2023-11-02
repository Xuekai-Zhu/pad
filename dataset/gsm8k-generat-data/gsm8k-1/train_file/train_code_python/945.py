def solution():
    """Ruby is taking dance lessons. They cost $75 for 10 classes in one pack. She can add additional classes at the price of 1/3 more than the average price of a class on the lesson in the pack. if she takes 13 total classes, how much does she pay?"""
    pack_price = 75
    pack_classes = 10
    additional_classes = 3
    total_classes = 13
    average_price = pack_price / pack_classes
    additional_price = average_price + (1/3 * average_price)
    additional_classes_price = (total_classes - pack_classes) * additional_price
    total_price = pack_price + additional_classes_price
    result = total_price
    return result

print(solution())