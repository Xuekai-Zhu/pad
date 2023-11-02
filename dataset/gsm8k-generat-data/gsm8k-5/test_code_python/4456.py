def solution():
    sheets_per_class_per_week = 200 * 5  # Each class uses 200 sheets per day and there are 5 school days
    total_sheets_per_week = 9000  # The school uses a total of 9000 sheets of paper every week

    # Calculate the number of classes in the school
    num_classes = total_sheets_per_week / sheets_per_class_per_week
    result = num_classes
    return result

print(solution())