def solution():
    # Define the initial volume and the growth factor
    initial_volume = 500
    growth_factor = 2/5

    # Calculate the volume after 1 hour and 2 hours
    volume_after_1_hour = initial_volume * (1 + growth_factor)
    volume_after_2_hours = volume_after_1_hour * (1 + growth_factor)

    result = volume_after_2_hours
    return result

print(solution())