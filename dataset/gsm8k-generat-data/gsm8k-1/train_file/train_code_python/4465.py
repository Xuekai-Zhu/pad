def solution():
    """Lucas' father offers to pay him $2 for each window in the house that he cleans. Each floor of Lucas' house has 3 windows; Lucas lives in a 3-story house. To get Lucas to finish the job faster, his father tells him that he will subtract $1 for every 3 days that pass without Lucas finishing the job. In 6 days, Lucas finishes cleaning all the windows in the house. How much will his father pay him, in dollars?"""
    windows_per_floor = 3
    num_floors = 3
    num_windows = windows_per_floor * num_floors
    base_pay = 2 * num_windows
    days_to_finish = 6
    days_late = max(days_to_finish - 3, 0)
    late_penalty = days_late / 3
    final_pay = base_pay - late_penalty
    result = final_pay
    return result

print(solution())