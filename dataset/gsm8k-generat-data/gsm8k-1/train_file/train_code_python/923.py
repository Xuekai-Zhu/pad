def solution():
    """There are 8 loads of laundry that need to be washed. Each load of laundry takes around 45 minutes to complete in the wash cycle and 1 hour in the dry cycle. How long, in hours, will it take to complete the entire set of laundry?"""
    loads_of_laundry = 8
    wash_time = 0.75  # 45 minutes to decimal of an hour
    dry_time = 1
    total_time = loads_of_laundry * (wash_time + dry_time)
    result = total_time
    return result

print(solution())