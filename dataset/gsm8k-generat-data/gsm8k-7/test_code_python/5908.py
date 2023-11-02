def solution():
    num_rows = 4
    num_columns = 5
    time_per_tree = 6
    num_helpers = 1  # Jack gets one helper

    # Calculate the total number of trees in the grove
    total_trees = num_rows * num_columns

    # Calculate the total time it would take Jack alone to clean all the trees
    total_time = total_trees * time_per_tree

    # Calculate the total time with the helper
    total_time_helper = total_time / (num_helpers + 1)

    # Convert total time to hours
    total_time_hours = total_time_helper / 60

    result = total_time_hours
    return result

print(solution())