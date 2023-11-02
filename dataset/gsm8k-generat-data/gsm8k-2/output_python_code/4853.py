def solution():
    """In Zeoland the fine for speeding is $16 for each mile per hour the driver is traveling over the posted speed limit. In Zeoland, Jed was fined $256 for speeding on a road with a posted speed limit of 50 mph. Jed was fined for traveling at what speed in miles per hour?"""
    fine_amount = 256
    speed_limit = 50
    fine_per_mph_over = 16
    mph_over = (fine_amount / fine_per_mph_over) / speed_limit
    fined_speed = mph_over + speed_limit
    result = fined_speed
    return result

print(solution())