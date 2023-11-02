def solution():
    """Aubriella is pouring water into a 50-gallon fish tank at the rate of 1 gallon every 20 seconds. How many more gallons will she have to pour into the tank to fill the tank if she poured water into the fish tank for 6 minutes?"""
    tank_size = 50
    filling_rate = 1/20 # gallons per second
    filling_time = 6*60 # seconds
    total_filled = filling_rate * filling_time
    remaining_amount = tank_size - total_filled
    result = remaining_amount
    return result

print(solution())