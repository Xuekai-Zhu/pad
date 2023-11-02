def solution():
    weekdays_classes = 2  # The club offers 2 classes on weekdays
    weekend_classes = 4 * 2  # The club offers 4 classes on each weekend day
    total_classes = weekdays_classes * 5 + weekend_classes * 5  # Each class has room for 5 people
    weeks = 3  # The classes will take place for 3 weeks

    # Calculate the total number of people who can take classes in 3 weeks
    total_people = total_classes * weeks
    result = total_people
    return result

print(solution())