def solution():
    """The Diving Club offers 2 beginning diving classes on weekdays and 4 beginning classes on each day of the weekend. Each class has room for 5 people. How many people can take classes in 3 weeks?"""
    # Define the number of beginning diving classes offered
    WEEKDAY_CLASSES = 2
    WEEKEND_CLASSES = 4

    # Define the class capacity
    CLASS_CAPACITY = 5

    # Calculate the total number of classes offered in 3 weeks
    total_classes = (WEEKDAY_CLASSES * 5) + (WEEKEND_CLASSES * 2 * 3)

    # Calculate the total number of people that can take classes
    total_capacity = total_classes * CLASS_CAPACITY

    # Display the total number of people that can take classes
    result = total_capacity
    return result

print(solution())