def solution():
    total_school_hours = 7.5  # Keegan is in school for 7.5 hours each day
    num_classes = 7  # Keegan is taking 7 classes
    combined_history_chem_hours = 1.5  # Keegan has history and chemistry classes for a combined 1.5 hours

    # Calculate the total number of hours Keegan spends in all his other classes
    total_other_class_hours = total_school_hours - combined_history_chem_hours
    # Divide by the number of other classes to get the average time spent in each class
    avg_class_time = total_other_class_hours / (num_classes - 2)
    # Convert to minutes
    avg_class_time = avg_class_time * 60
    result = avg_class_time
    return result

print(solution())