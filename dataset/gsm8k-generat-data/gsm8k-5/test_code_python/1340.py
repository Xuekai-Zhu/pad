def solution():
    max_riding_time = 6  # William can ride his horse for a maximum of 6 hours a day
    full_days = 2  # William only used the maximum riding time twice
    short_days = 2  # William rode his horse for only 1.5 hours on two days
    half_days = 2  # William rode for half the maximum time on the remaining two days

    # Calculate the total riding time on the full days
    full_day_riding_time = full_days * max_riding_time

    # Calculate the total riding time on the short days
    short_day_riding_time = short_days * 1.5

    # Calculate the total riding time on the half days
    half_day_riding_time = half_days * (max_riding_time / 2)

    # Calculate the total riding time over the 6 days
    total_riding_time = full_day_riding_time + short_day_riding_time + half_day_riding_time
    result = total_riding_time
    
    return result

print(solution())