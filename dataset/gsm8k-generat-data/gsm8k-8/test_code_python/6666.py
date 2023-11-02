def solution():
    # Calculate the total number of classes
    total_classes = 2 + 1 + 2  # 2 three-hour classes, 1 four-hour class, 2 total classes per week

    # Multiply the total number of classes by the number of weeks to get the total class time
    class_time = total_classes * 24  # 24 weeks

    # Add the time spent on small group work
    total_time = class_time + 4 * 24  # 4 hours per week for 24 weeks

    result = total_time
    return result

print(solution())