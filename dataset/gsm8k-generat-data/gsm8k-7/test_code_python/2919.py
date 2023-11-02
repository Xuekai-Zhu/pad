def solution():
    weekdays_classes = 2
    weekend_classes = 4
    class_capacity = 5
    num_weeks = 3

    # Calculate the total number of classes
    total_classes = (weekdays_classes * 5) + (weekend_classes * 2)

    # Calculate the total number of people who can take classes
    total_people = total_classes * class_capacity * num_weeks
    result = total_people
    return result

print(solution())