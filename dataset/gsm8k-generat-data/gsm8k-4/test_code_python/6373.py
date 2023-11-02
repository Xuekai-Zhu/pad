def solution():
    """Tim's website got 100 visitors a day for the first 6 days and then on the last day of the week it got twice as many visitors as every other day combined. If he gets $.01 per visit how much did he make that week?"""
    # Define the number of visitors per day for the first 6 days
    visitors_per_day = 100

    # Calculate the total number of visitors for the first 6 days
    total_visitors_first_6_days = visitors_per_day * 6

    # Calculate the total number of visitors on the last day
    total_visitors_last_day = total_visitors_first_6_days * 2

    # Calculate the total number of visitors for the week
    total_visitors = total_visitors_first_6_days + total_visitors_last_day

    # Calculate the total earnings for the week
    earnings = total_visitors * 0.01

    # Return the result
    result = earnings
    return result

print(solution())