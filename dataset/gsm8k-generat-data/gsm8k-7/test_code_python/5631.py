def solution():
    num_classes = 4
    class_length = 2
    dropped_class = 1

    # Calculate the total hours of classes before dropping one
    total_hours = num_classes * class_length

    # Calculate the total hours of classes after dropping one
    new_num_classes = num_classes - dropped_class
    new_total_hours = new_num_classes * class_length

    # Calculate the hours of classes per day
    hours_per_day = new_total_hours / 5 # Assuming 5 school days per week
    result = hours_per_day
    return result

print(solution())