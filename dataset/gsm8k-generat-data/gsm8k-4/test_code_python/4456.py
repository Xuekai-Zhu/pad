def solution():
    """Each class uses 200 sheets of paper per day. The school uses a total of 9000 sheets of paper every week. If there are 5 days of school days, how many classes are there in the school?"""
    # Define the number of sheets used per week
    sheets_per_week = 9000

    # Define the number of school days per week
    days_per_week = 5

    # Define the number of sheets used per class per week
    sheets_per_class_per_week = 200 * days_per_week

    # Calculate the number of classes in the school
    classes = sheets_per_week / sheets_per_class_per_week

    # Round up to the nearest integer
    classes = int(classes) + 1

    result = classes
    return result

print(solution())