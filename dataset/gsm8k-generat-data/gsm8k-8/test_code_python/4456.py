def solution():
    # Calculate the total sheets of paper used in a week
    total_sheets_per_week = 9000

    # Calculate the sheets of paper used in a day
    sheets_per_day = 200

    # Calculate the total sheets of paper used in a week by one class
    total_sheets_per_class_per_week = sheets_per_day * 5

    # Calculate the number of classes in the school
    num_classes = total_sheets_per_week / total_sheets_per_class_per_week
    result = num_classes
    return result

print(solution())