def solution():
    # Calculate the total amount of water wasted in one hour
    drip_per_hour = 10 * 60  # drips per minute times 60 minutes
    water_wasted = drip_per_hour * 0.05  # volume of one drop is 0.05mL
    result = water_wasted
    return result

print(solution())