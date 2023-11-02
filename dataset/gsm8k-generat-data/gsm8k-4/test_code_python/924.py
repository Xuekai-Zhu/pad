def solution():
    """There are 8 loads of laundry that need to be washed. Each load of laundry takes around 45 minutes to complete in the wash cycle and 1 hour in the dry cycle. How long, in hours, will it take to complete the entire set of laundry?"""
    # Define the time it takes to wash and dry one load of laundry
    wash_time = 0.75  # 45 minutes = 0.75 hours
    dry_time = 1.0

    # Calculate the total time to wash and dry all the loads of laundry
    total_wash_time = wash_time * 8
    total_dry_time = dry_time * 8
    total_time = total_wash_time + total_dry_time

    # return the result in hours
    result = total_time
    return result

print(solution())