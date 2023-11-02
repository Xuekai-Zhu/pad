def solution():
    """The Diving Club offers 2 beginning diving classes on weekdays and 4 beginning classes on each day of the weekend. Each class has room for 5 people. How many people can take classes in 3 weeks?"""
    # Define the number of beginning classes on weekdays and weekends
    weekday_classes = 2
    weekend_classes = 4

    # Define the capacity of each class
    class_capacity = 5

    # Calculate the number of people who can take classes each day
    daily_capacity = weekday_classes + weekend_classes * 2

    # Calculate the total number of people who can take classes in 3 weeks
    total_capacity = daily_capacity * 5 * 3

    # Return the result
    result = total_capacity
    return result

print(solution())