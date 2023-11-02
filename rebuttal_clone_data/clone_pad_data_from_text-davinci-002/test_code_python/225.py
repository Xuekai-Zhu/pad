def solution():
     """A washing machine uses 20 gallons of water for a heavy wash, 10 gallons of water for a regular wash, and 2 gallons of water for a light wash per load of laundry. If bleach is used, there is an extra light wash cycle added to rinse the laundry thoroughly. There are two heavy washes, three regular washes, and one light wash to do. Two of the loads need to be bleached. How many gallons of water will be needed?"""
     heavy_wash = 20
     regular_wash = 10
     light_wash = 2
     heavy_loads = 2
     regular_loads = 3
     light_loads = 1
     bleach_loads = 2
     total_water = (heavy_loads * heavy_wash) + (regular_loads * regular_wash) + (light_loads * light_wash) + (bleach_loads * light_wash)
     result = total_water
     return result

print(solution())