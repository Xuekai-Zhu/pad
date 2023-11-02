def solution():
    total_trees = 4 * 5  # Jack has a grove with 20 trees
    cleaning_time = 6  # It takes Jack 6 minutes to clean each tree

    # Calculate the total cleaning time for all the trees, without help
    total_cleaning_time = total_trees * cleaning_time

    # Calculate the total cleaning time with help
    total_cleaning_time_with_help = total_cleaning_time / 2

    # Convert the total cleaning time to hours
    cleaning_hours = total_cleaning_time_with_help / 60
    result = cleaning_hours
    return result

print(solution())