def solution():
    """On a normal day, Julia can run a mile in 10 minutes. However, today she decided to wear her new shoes to run. They were uncomfortable and slowed her mile down to 13 minutes. How much longer would it take Julia to run 5 miles in her new shoes than if she wore her old ones?"""
    # Define the time it takes Julia to run one mile
    old_time = 10
    new_time = 13

    # Calculate the time it would take Julia to run 5 miles with her old shoes
    old_total_time = old_time * 5

    # Calculate the time it would take Julia to run 5 miles with her new shoes
    new_total_time = new_time * 5

    # Calculate the difference in time between the two options
    time_difference = new_total_time - old_total_time

    # return the result
    result = time_difference
    return result

print(solution())