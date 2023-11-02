def solution():
    """Keegan is in school for 7.5 hours each day and he is taking 7 classes. He has history and chemistry classes for a combined total of 1.5 hours. How many minutes does Keegan spend in one of his other classes on average?"""
    # Define the total number of hours Keegan spends in class each day
    total_hours = 7.5

    # Define the number of hours Keegan spends in history and chemistry classes combined
    history_chem_hours = 1.5

    # Define the number of classes Keegan takes besides history and chemistry
    other_classes = 7 - 2

    # Calculate the average number of minutes Keegan spends in one of his other classes
    other_class_minutes = ((total_hours - history_chem_hours) / other_classes) * 60

    # return the result
    result = other_class_minutes
    return result

print(solution())