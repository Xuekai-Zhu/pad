def solution():
    """There are 8 loads of laundry that need to be washed. Each load of laundry takes around 45 minutes to complete in the wash cycle and 1 hour in the dry cycle. How long, in hours, will it take to complete the entire set of laundry?"""
    # Define the time for one load of laundry
    WASH_TIME = 0.75 # 45 minutes, converted to hours
    DRY_TIME = 1

    # Calculate the total time for all 8 loads of laundry
    total_time = (WASH_TIME + DRY_TIME) * 8

    # Display the total time in hours
    result = total_time
    return result

print(solution())