def solution():
    # Calculate the total number of beginning diving classes
    total_classes = 2 * 5 + 4 * 2 * 5  # 2 classes on each weekday and 4 classes on each day of the weekend
    # Calculate the total number of people that can take the classes in 3 weeks
    total_people = total_classes * 5 * 3  # 5 people can take each class, and there are 3 weeks
    result = total_people
    return result

print(solution())