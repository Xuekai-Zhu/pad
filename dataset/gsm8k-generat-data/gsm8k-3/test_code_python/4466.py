def solution():
    """Lucas' father offers to pay him $2 for each window in the house that he cleans. Each floor of Lucas' house has 3 windows; Lucas lives in a 3-story house. To get Lucas to finish the job faster, his father tells him that he will subtract $1 for every 3 days that pass without Lucas finishing the job. In 6 days, Lucas finishes cleaning all the windows in the house. How much will his father pay him, in dollars?"""
    # Define the initial payment per window and the penalty for delaying the job
    INITIAL_PAYMENT = 2
    DELAY_PENALTY = 1

    # Define the number of floors and windows per floor
    FLOORS = 3
    WINDOWS_PER_FLOOR = 3

    # Define the number of days it took Lucas to finish the job
    DAYS = 6

    # Calculate the total number of windows in the house
    total_windows = FLOORS * WINDOWS_PER_FLOOR

    # Calculate the initial payment before any penalty
    initial_payment = total_windows * INITIAL_PAYMENT

    # Calculate the number of days past the deadline
    days_past_deadline = DAYS - 3

    # Calculate the total penalty for delaying the job, if any
    penalty = max(0, days_past_deadline // 3) * DELAY_PENALTY

    # Calculate the final payment to Lucas
    final_payment = initial_payment - penalty

    # Display the final payment
    result = final_payment
    return result

print(solution())