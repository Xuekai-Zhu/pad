def solution():
    """Amelia has laundry to do. She has a load of whites that will take 72 minutes in the washing machine and 50 minutes in the dryer. She has a load of darks that will take 58 minutes in the washing machine and 65 minutes in the dryer. She has a load of colors that will take 45 minutes in the washer and 54 minutes in the dryer. If she does one load at a time, how long will it take her to wash and dry all three loads, in minutes?"""
    wash_times = [72, 58, 45]
    dry_times = [50, 65, 54]
    total_time = sum(wash_times) + sum(dry_times)
    result = total_time
    return result

print(solution())