def solution():
    """Kim takes 4 classes in school that last 2 hours each.  She drops 1 class.  How many hours of classes does she have now have per day?"""
    # Define the number of classes and hours per class
    NUM_CLASSES = 4
    HOURS_PER_CLASS = 2

    # Define the number of classes Kim drops
    NUM_CLASSES_DROPPED = 1

    # Calculate the total hours of classes before dropping a class
    total_hours_before = NUM_CLASSES * HOURS_PER_CLASS

    # Calculate the total hours of classes after dropping a class
    total_hours_after = (NUM_CLASSES - NUM_CLASSES_DROPPED) * HOURS_PER_CLASS

    # Calculate the hours of classes per day
    hours_per_day = total_hours_after / 5

    # Display the hours of classes per day
    result = hours_per_day
    return result

print(solution())