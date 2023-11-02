def solution():
    # Define the number of classes and their duration
    num_classes = 4
    class_duration = 2

    # Calculate the total duration of classes before dropping one
    total_duration = num_classes * class_duration

    # Drop one class
    num_classes -= 1

    # Calculate the new total duration of classes
    new_total_duration = num_classes * class_duration

    # Calculate the difference in duration
    difference = total_duration - new_total_duration

    # Convert the difference from hours to minutes
    difference_in_minutes = difference * 60

    # Calculate the new duration per day
    duration_per_day = (new_total_duration * 5) / 7

    # Add the difference back to get the duration per day before dropping a class
    duration_per_day += difference_in_minutes / 60

    result = duration_per_day
    return result

print(solution())