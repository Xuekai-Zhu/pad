def solution():
    heavy_wash_gallons = 20
    regular_wash_gallons = 10
    light_wash_gallons = 2

    num_heavy_washes = 2
    num_regular_washes = 3
    num_light_washes = 1

    num_bleached_loads = 2

    # Calculate the total gallons of water for all heavy washes
    total_heavy_wash_gallons = num_heavy_washes * heavy_wash_gallons

    # Calculate the total gallons of water for all regular washes
    total_regular_wash_gallons = num_regular_washes * regular_wash_gallons

    # Calculate the total gallons of water for all light washes
    total_light_wash_gallons = (num_light_washes + num_bleached_loads) * light_wash_gallons

    # Calculate the total gallons of water needed
    total_gallons_needed = total_heavy_wash_gallons + total_regular_wash_gallons + total_light_wash_gallons
    result = total_gallons_needed
    return result

print(solution())