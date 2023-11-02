def solution():
    """Rob planned on spending three hours reading in preparation for his literature exam. If he ends up spending only three-quarters of this time reading, and he reads a page every fifteen minutes, how many pages did he read in this time?"""
    # Define the total time Rob planned on spending reading, in minutes
    planned_time = 3 * 60

    # Calculate the actual time Rob spent reading, in minutes
    actual_time = planned_time * 0.75

    # Calculate the number of pages Rob read based on his actual reading time
    pages_read = actual_time / 15

    result = pages_read
    return result

print(solution())