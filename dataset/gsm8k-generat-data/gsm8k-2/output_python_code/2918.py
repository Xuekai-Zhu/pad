def solution():
    """The Diving Club offers 2 beginning diving classes on weekdays and 4 beginning classes on each day of the weekend. Each class has room for 5 people. How many people can take classes in 3 weeks?"""
    weekdays_classes = 2 * 5  # 2 classes per day on weekdays
    weekend_classes = 4 * 5 * 2  # 4 classes per day on each weekend day
    total_classes = weekdays_classes * 5 + weekend_classes * 2  # 3 weeks = 15 weekdays and 6 weekend days
    total_people = total_classes * 5  # each class has room for 5 people
    result = total_people
    return result

print(solution())