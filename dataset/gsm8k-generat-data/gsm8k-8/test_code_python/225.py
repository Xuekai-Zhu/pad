def solution():
    # Calculate the total gallons of water used for heavy washes
    heavy_wash_gallons = 20 * 2

    # Calculate the total gallons of water used for regular washes
    regular_wash_gallons = 10 * 3

    # Calculate the total gallons of water used for light washes
    light_wash_gallons = 2

    # Calculate the total gallons of water used for bleaching
    bleach_gallons = 2 * light_wash_gallons

    # Calculate the total gallons of water needed
    total_gallons = heavy_wash_gallons + regular_wash_gallons + (1 + 2) * light_wash_gallons + bleach_gallons

    result = total_gallons
    return result

print(solution())