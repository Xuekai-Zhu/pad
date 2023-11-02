def solution():
    """If farmer Steven can use his tractor to plow up to 10 acres of farmland per day, or use the same tractor to mow up to 12 acres of grassland per day, how long would it take him to plow his 55 acres of farmland and mow his 30 acres of grassland?"""
    # Define the total area of farmland and grassland
    farmland_area = 55
    grassland_area = 30

    # Define the plowing speed and mowing speed
    plowing_speed = 10
    mowing_speed = 12

    # Calculate the number of days needed to plow the farmland
    plowing_days = farmland_area / plowing_speed

    # Calculate the number of days needed to mow the grassland
    mowing_days = grassland_area / mowing_speed

    # Calculate the total number of days needed to complete both tasks
    total_days = plowing_days + mowing_days

    result = total_days
    return result

print(solution())