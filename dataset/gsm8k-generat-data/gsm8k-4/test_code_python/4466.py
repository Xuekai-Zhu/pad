def solution():
    """Lucas' father offers to pay him $2 for each window in the house that he cleans. Each floor of Lucas' house has 3 windows; Lucas lives in a 3-story house. To get Lucas to finish the job faster, his father tells him that he will subtract $1 for every 3 days that pass without Lucas finishing the job. In 6 days, Lucas finishes cleaning all the windows in the house. How much will his father pay him, in dollars?"""
    # Define the number of floors in the house and the number of windows per floor
    floors = 3
    windows_per_floor = 3

    # Calculate the total number of windows in the house
    total_windows = floors * windows_per_floor

    # Define the initial pay rate and the rate of decrease for every 3 days
    initial_pay_rate = 2
    pay_rate_decrease = 1

    # Define the number of days it took Lucas to clean all the windows
    days_taken = 6

    # Calculate the final pay rate based on the number of days taken to finish the job
    final_pay_rate = max(0, initial_pay_rate - (pay_rate_decrease * ((days_taken - 1) // 3)))

    # Calculate the total amount of money Lucas will be paid
    total_pay = final_pay_rate * total_windows

    result = total_pay
    return result

print(solution())