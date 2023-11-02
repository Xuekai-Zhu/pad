def solution():
    
    # Define the number of periods and extra classes per week
    periods_per_day = 6
    extra_classes_per_week = 2

    # Define the length of each class in minutes
    class_length = 40

    # Define the number of days per week
    days_per_week = 5

    # Calculate the total number of extra classes per week
    extra_classes_per_week = classes_per_week * extra_classes_per_week

    # Calculate the total time spent learning per week
    total_learning_time = (extra_classes_per_week * class_length) / 16

    # Calculate the total hours spent learning per week
    total_learning_hours = total_learning_time / 60

    # Display the total hours spent learning per week
    result = total_learning_hours
    return result

print(solution())