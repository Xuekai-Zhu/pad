def solution():
    """Gentry assembled a new 24 foot round pool in her backyard. To fill the pool with water, she used four hoses. Two of the hoses each deliver water at a rate of 2 gallons per minute. The other two hoses each deliver water at a rate of 3 gallons per minute. With a volume of 15,000 gallons, how many hours will it take to fill the pool?"""
    # Define the diameter and radius of the pool in feet
    pool_diameter = 24
    pool_radius = pool_diameter / 2

    # Calculate the volume of the pool in cubic feet
    pool_volume = (4/3) * 3.14 * (pool_radius**3)

    # Convert the volume to gallons
    pool_volume_gallons = pool_volume * 7.5

    # Define the flow rates of the hoses in gallons per minute
    hose1_rate = 2
    hose2_rate = 2
    hose3_rate = 3
    hose4_rate = 3

    # Calculate the total flow rate of all four hoses
    total_flow_rate = hose1_rate + hose2_rate + hose3_rate + hose4_rate

    # Calculate the time it will take to fill the pool in minutes
    time_to_fill_minutes = pool_volume_gallons / total_flow_rate

    # Convert the time to fill to hours
    time_to_fill_hours = time_to_fill_minutes / 60

    # Round the result to 1 decimal place
    result = round(time_to_fill_hours, 1)
    return result

print(solution())