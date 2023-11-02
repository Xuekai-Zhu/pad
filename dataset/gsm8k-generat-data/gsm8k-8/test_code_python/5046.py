def solution():
    # Define given variables
    pool_radius = 24 / 2 # Convert diameter to radius
    pool_volume = 15000
    hose1_rate = 2
    hose2_rate = 2
    hose3_rate = 3
    hose4_rate = 3

    # Calculate pool surface area and volume
    pool_surface_area = 3.14 * (pool_radius ** 2)
    pool_height = pool_volume / pool_surface_area

    # Calculate total water flow rate in gallons per minute
    total_flow_rate = (hose1_rate + hose2_rate + hose3_rate + hose4_rate)

    # Calculate total time in hours to fill the pool
    total_time = (pool_volume / total_flow_rate) / 60

    result = total_time
    return result

print(solution())