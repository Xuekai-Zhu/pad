def solution():
    pool_radius = 24/2  # radius of the pool is half of the diameter (in feet)
    pool_volume = (4/3) * 3.14 * (pool_radius**3) * 7.48  # volume of the pool in gallons

    # Calculate the total flow rate of the four hoses
    total_flow_rate = 2 * 2 + 2 * 3  # two hoses deliver 2 gallons per minute and two hoses deliver 3 gallons per minute

    # Calculate the time required to fill the pool
    time_to_fill = pool_volume / total_flow_rate / 60  # converted to hours

    result = time_to_fill
    return result

print(solution())