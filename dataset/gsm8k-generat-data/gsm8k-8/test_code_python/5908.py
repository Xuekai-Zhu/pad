def solution():
    # Define the size of the grove
    grove_size = 4 * 5

    # Define the time it takes to clean a tree
    time_per_tree = 6

    # Calculate the total time it would take for Jack to clean the grove himself
    total_time = grove_size * time_per_tree

    # Get the time it would take with help, which is half the original time
    time_with_help = total_time / 2

    # Convert the total time to hours
    hours = time_with_help / 60
    result = hours
    return result

print(solution())