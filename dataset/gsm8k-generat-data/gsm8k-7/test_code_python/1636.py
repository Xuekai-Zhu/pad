def solution():
    total_hours = 7.5
    num_classes = 7
    history_chem_hours = 1.5

    # Calculate the total hours spent on all of Keegan's classes except history and chemistry
    total_other_hours = total_hours - history_chem_hours

    # Calculate the number of hours spent on each other class on average
    avg_hours_per_class = total_other_hours / (num_classes - 2)

    # Convert the average hours per class to minutes
    avg_minutes_per_class = avg_hours_per_class * 60
    result = avg_minutes_per_class
    return result

print(solution())