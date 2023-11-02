def solution():
    # Calculate the total amount of water needed for heavy washes
    heavy_washes = 2  # There are two heavy washes to do
    water_per_heavy_wash = 20  # The washing machine uses 20 gallons of water for a heavy wash
    total_water_for_heavy_washes = heavy_washes * water_per_heavy_wash

    # Calculate the total amount of water needed for regular washes
    regular_washes = 3  # There are three regular washes to do
    water_per_regular_wash = 10  # The washing machine uses 10 gallons of water for a regular wash
    total_water_for_regular_washes = regular_washes * water_per_regular_wash

    # Calculate the total amount of water needed for light washes
    light_washes = 1  # There is one light wash to do
    water_per_light_wash = 2  # The washing machine uses 2 gallons of water for a light wash
    total_water_for_light_washes = light_washes * water_per_light_wash

    # Calculate the total amount of water needed for bleaching
    bleached_loads = 2  # Two loads need to be bleached, adding an extra light wash cycle
    total_water_for_bleaching = bleached_loads * water_per_light_wash

    # Calculate the total amount of water needed for all loads of laundry
    total_water = total_water_for_heavy_washes + total_water_for_regular_washes + total_water_for_light_washes + total_water_for_bleaching
    result = total_water
    return result

print(solution())