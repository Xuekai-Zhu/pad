def solution():
    """Gentry assembled a new 24 foot round pool in her backyard.  To fill the pool with water, she used four hoses.  Two of the hoses each deliver water at a rate of 2 gallons per minute.  The other two hoses each deliver water at a rate of 3 gallons per minute.  With a volume of 15,000 gallons, how many hours will it take to fill the pool?"""
    # Define the radius of the pool in feet
    radius = 24 / 2

    # Calculate the volume of the pool in cubic feet
    volume = (4/3) * 3.14 * (radius**3)

    # Convert the volume of the pool to gallons
    volume_gallons = volume * 7.48

    # Define the flow rates of the four hoses in gallons per minute
    flow_rate_1 = 2
    flow_rate_2 = 2
    flow_rate_3 = 3
    flow_rate_4 = 3

    # Calculate the total flow rate of all four hoses combined in gallons per minute
    total_flow_rate = flow_rate_1 + flow_rate_2 + flow_rate_3 + flow_rate_4

    # Calculate the time it will take to fill the pool in minutes
    time_minutes = volume_gallons / total_flow_rate

    # Convert the time to hours
    time_hours = time_minutes / 60

    # Display the time it will take to fill the pool
    result = time_hours
    return result

print(solution())