def solution():
    """The Diving Club offers 2 beginning diving classes on weekdays and 4 beginning classes on each day of the weekend. Each class has room for 5 people. How many people can take classes in 3 weeks?"""
    weekdays = 2
    weekend_days = 2 # Saturday and Sunday
    weekend_classes = 4
    class_size = 5
    weeks = 3
    total_classes = (weekdays * 5) + (weekend_days * weekend_classes * 5)
    total_students = total_classes * weeks
    result = total_students
    return result

print(solution())