def solution():
    """Kenny played basketball last week. He ran for twice as long as he played basketball, and he practiced on the trumpet for twice as long as he ran. If he practiced on the trumpet for 40 hours, how many hours did Kenny play basketball last week?"""
    # Define the time ratios
    BASKETBALL_TO_RUN = 1
    RUN_TO_TRUMPET = 1/2
    TRUMPET_TO_RUN = 2
    TRUMPET_TO_BASKETBALL = 4

    # Calculate the total time Kenny spent on trumpet and running
    total_trumpet_and_run = 40 + (40 * RUN_TO_TRUMPET * TRUMPET_TO_RUN)
    total_run = total_trumpet_and_run / (RUN_TO_TRUMPET + TRUMPET_TO_RUN)
    total_basketball = total_run * BASKETBALL_TO_RUN

    # Display the time spent playing basketball
    result = total_basketball
    return result

print(solution())