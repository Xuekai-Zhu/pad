def solution():
    """A washing machine uses 20 gallons of water for a heavy wash, 10 gallons of water for a regular wash, and 2 gallons of water for a light wash per load of laundry. If bleach is used, there is an extra light wash cycle added to rinse the laundry thoroughly. There are two heavy washes, three regular washes, and one light wash to do. Two of the loads need to be bleached. How many gallons of water will be needed?"""
    heavy_wash_gallons = 20
    regular_wash_gallons = 10
    light_wash_gallons = 2
    bleached_loads = 2
    
    total_gallons = (heavy_wash_gallons * 2) + (regular_wash_gallons * 3) + (light_wash_gallons * 1) + \
                    (light_wash_gallons * bleached_loads)
    
    result = total_gallons
    return result

print(solution())