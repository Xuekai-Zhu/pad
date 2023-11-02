def solution():
    """Kim takes 4 classes in school that last 2 hours each. She drops 1 class. How many hours of classes does she have now have per day?"""
    num_classes = 4
    hours_per_class = 2
    classes_dropped = 1
    remaining_classes = num_classes - classes_dropped
    total_hours = remaining_classes * hours_per_class
    hours_per_day = total_hours / 5 # assuming 5 school days per week
    result = hours_per_day
    return result

print(solution())