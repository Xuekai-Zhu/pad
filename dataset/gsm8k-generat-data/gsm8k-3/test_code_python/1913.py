def solution():
    """If farmer Steven can use his tractor to plow up to 10 acres of farmland per day, or use the same tractor to mow up to 12 acres of grassland per day, how long would it take him to plow his 55 acres of farmland and mow his 30 acres of grassland?"""
    # Define the number of acres to be plowed and mowed
    farmland_acres = 55
    grassland_acres = 30

    # Define the tractor's plowing and mowing capacities
    plowing_capacity = 10
    mowing_capacity = 12

    # Calculate the number of days needed to plow the farmland
    plowing_days = farmland_acres / plowing_capacity

    # Calculate the number of days needed to mow the grassland
    mowing_days = grassland_acres / mowing_capacity

    # Calculate the total number of days needed
    total_days = plowing_days + mowing_days

    # Display the total number of days needed
    result = total_days
    return result

print(solution())