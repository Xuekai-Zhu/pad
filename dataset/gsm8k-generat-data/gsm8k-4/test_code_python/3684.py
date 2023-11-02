def solution():
    """Amelia has laundry to do. She has a load of whites that will take 72 minutes in the washing machine and 50 minutes in the dryer. She has a load of darks that will take 58 minutes in the washing machine and 65 minutes in the dryer. She has a load of colors that will take 45 minutes in the washer and 54 minutes in the dryer. If she does one load at a time, how long will it take her to wash and dry all three loads, in minutes?"""
    # Define the duration of each load
    whites_wash_time = 72
    whites_dry_time = 50
    darks_wash_time = 58
    darks_dry_time = 65
    colors_wash_time = 45
    colors_dry_time = 54

    # Calculate the total duration of washing and drying one load at a time
    total_time = (whites_wash_time + whites_dry_time) + (darks_wash_time + darks_dry_time) + (colors_wash_time + colors_dry_time)

    # return the result
    result = total_time
    return result

print(solution())