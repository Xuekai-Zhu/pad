def solution():
    """Keegan is in school for 7.5 hours each day and he is taking 7 classes. He has history and chemistry classes for a combined total of 1.5 hours. How many minutes does Keegan spend in one of his other classes on average?"""
    total_class_time = 7.5 * 60  # in minutes
    history_chem_time = 1.5 * 60  # in minutes
    other_class_time = total_class_time - history_chem_time
    num_other_classes = 7 - 2  # subtracting history and chemistry classes
    avg_other_class_time = other_class_time / num_other_classes
    result = avg_other_class_time
    return result

print(solution())