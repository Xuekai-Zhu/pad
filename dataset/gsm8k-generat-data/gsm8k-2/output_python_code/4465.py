def solution():
    """Lucas' father offers to pay him $2 for each window in the house that he cleans. Each floor of Lucas' house has 3 windows; Lucas lives in a 3-story house. To get Lucas to finish the job faster, his father tells him that he will subtract $1 for every 3 days that pass without Lucas finishing the job. In 6 days, Lucas finishes cleaning all the windows in the house. How much will his father pay him, in dollars?"""
    windows_per_floor = 3
    total_floors = 3
    total_windows = windows_per_floor * total_floors
    payment_per_window = 2
    days_to_finish = 6
    days_passed = 3
    payment_per_day = 1
    total_payment = total_windows * payment_per_window
    if days_to_finish > days_passed:
        days_late = days_to_finish - days_passed
        payment_late = (days_late // 3) * payment_per_day
        total_payment -= payment_late

    result = total_payment
    return result

print(solution())