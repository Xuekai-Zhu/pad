def solution():
    # Let's say Chase drives at speed x.
    # Therefore, Cameron drives at speed 2x and Danielle drives at speed 3(2x) = 6x.
    # Let's also say the distance from Granville to Salisbury is d.
    d = 1  # We can assume any arbitrary value for d, as it will cancel out in our calculations.

    # If Danielle takes 30 minutes to travel from Granville to Salisbury, then her speed is d/(30/60) = 2d miles per hour.
    # Therefore, 2d = 6x, or x = d/3.
    # This means Chase drives at speed d/3.
    
    # The time it takes Chase to travel from Granville to Salisbury is d/(d/3) = 3 hours.
    # However, we need to convert hours to minutes.
    time_in_minutes = 3 * 60
    result = time_in_minutes
    return result

print(solution())