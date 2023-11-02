def solution():
    """On a normal day, Julia can run a mile in 10 minutes. However, today she decided to wear her new shoes to run. They were uncomfortable and slowed her mile down to 13 minutes. How much longer would it take Julia to run 5 miles in her new shoes than if she wore her old ones?"""
    # Define Julia's normal pace
    NORMAL_PACE = 10 # minutes per mile

    # Define Julia's pace with the new shoes
    NEW_SHOES_PACE = 13 # minutes per mile

    # Calculate the time it would take to run 5 miles with the old shoes
    old_shoes_time = 5 * NORMAL_PACE # minutes

    # Calculate the time it would take to run 5 miles with the new shoes
    new_shoes_time = 5 * NEW_SHOES_PACE # minutes

    # Calculate the difference in time
    difference = new_shoes_time - old_shoes_time

    # Display the difference in time
    result = difference
    return result

print(solution())