def solution():
    """A washing machine uses 20 gallons of water for a heavy wash, 10 gallons of water for a regular wash, and 2 gallons of water for a light wash per load of laundry. If bleach is used, there is an extra light wash cycle added to rinse the laundry thoroughly. There are two heavy washes, three regular washes, and one light wash to do. Two of the loads need to be bleached. How many gallons of water will be needed?"""
    heavy_washes = 2
    regular_washes = 3
    light_washes = 1
    bleached_loads = 2
    water_per_heavy_wash = 20
    water_per_regular_wash = 10
    water_per_light_wash = 2
    total_water = (heavy_washes * water_per_heavy_wash) + (regular_washes * water_per_regular_wash) + (
            light_washes * water_per_light_wash)
    if bleached_loads > 0:
        total_water += water_per_light_wash
    total_water *= 2  # because there are two loads to do
    result = total_water
    return result

print(solution())