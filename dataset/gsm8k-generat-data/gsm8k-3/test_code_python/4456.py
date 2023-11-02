def solution():
    """Each class uses 200 sheets of paper per day. The school uses a total of 9000 sheets of paper every week. If there are 5 days of school days, how many classes are there in the school?"""
    # Define the number of sheets of paper per class per week
    sheets_per_class = 200 * 5

    # Calculate the number of classes in the school
    classes = 9000 / sheets_per_class

    # Display the number of classes
    result = classes
    return result

print(solution())