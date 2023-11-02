def solution():
    """Keegan is in school for 7.5 hours each day and he is taking 7 classes. He has history and chemistry classes for a combined total of 1.5 hours. How many minutes does Keegan spend in one of his other classes on average?"""
    # Define the total number of hours Keegan spends in all his classes
    total_hours = 7.5

    # Define the number of hours Keegan spends in history and chemistry classes
    history_chem_hours = 1.5

    # Calculate the number of hours Keegan spends in his other classes
    other_hours = total_hours - history_chem_hours

    # Calculate the average number of minutes Keegan spends in one of his other classes
    minutes_per_class = (other_hours / (7 - 2)) * 60

    # Display the average number of minutes per class
    result = minutes_per_class
    return result

print(solution())