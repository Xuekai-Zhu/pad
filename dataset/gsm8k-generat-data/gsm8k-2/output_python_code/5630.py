def solution():
    """Kim takes 4 classes in school that last 2 hours each. She drops 1 class. How many hours of classes does she have now have per day?"""
    num_classes = 4
    class_length = 2
    dropped_class = 1
    total_class_time = num_classes * class_length
    new_class_time = total_class_time - (dropped_class * class_length)
    daily_class_time = new_class_time / num_classes
    result = daily_class_time
    return result

print(solution())