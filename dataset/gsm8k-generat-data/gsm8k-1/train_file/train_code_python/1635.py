def solution():
    """Keegan is in school for 7.5 hours each day and he is taking 7 classes. He has history and chemistry classes for a combined total of 1.5 hours. How many minutes does Keegan spend in one of his other classes on average?"""
    school_hours_per_day = 7.5
    num_classes = 7
    history_chem_hours = 1.5
    other_hours = school_hours_per_day - history_chem_hours
    num_other_classes = num_classes - 2
    minutes_per_class = (other_hours * 60) / num_other_classes
    result = minutes_per_class
    return result

print(solution())