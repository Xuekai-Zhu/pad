def solution():
    lawn_rate = 4.0
    weed_rate = 8.0
    sept_lawn_hours = 25
    sept_weed_hours = 3
    oct_lawn_hours = 25
    oct_weed_hours = 3

    # Calculate the total earned for mowing lawns in September and October
    total_lawn_earned = (sept_lawn_hours + oct_lawn_hours) * lawn_rate

    # Calculate the total earned for pulling weeds in September and October
    total_weed_earned = (sept_weed_hours + oct_weed_hours) * weed_rate

    # Calculate the total earned for both months
    total_earned = total_lawn_earned + total_weed_earned
    result = total_earned
    return result

print(solution())