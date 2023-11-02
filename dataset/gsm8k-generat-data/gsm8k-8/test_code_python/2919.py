def solution():
    # Calculate the total number of classes offered each week
    weekday_classes = 2 * 5 # 2 classes per weekday
    weekend_classes = 4 * 5 # 4 classes per day on weekend
    total_classes = weekday_classes + weekend_classes

    # Calculate the total number of people who can take classes each week
    max_people_per_week = total_classes * 5 # 5 people per class

    # Calculate the total number of people who can take classes in 3 weeks
    total_people_in_3_weeks = max_people_per_week * 3

    result = total_people_in_3_weeks
    return result

print(solution())