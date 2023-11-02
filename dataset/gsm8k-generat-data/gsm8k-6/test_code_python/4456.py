def solution():
    # Calculate the total number of sheets of paper used by one class in a week
    weekly_paper_per_class = 200 * 5  # 200 sheets of paper used per day, 5 school days in a week

    # Calculate the number of classes in the school
    num_classes = 9000 / weekly_paper_per_class
    result = num_classes
    return result

print(solution())