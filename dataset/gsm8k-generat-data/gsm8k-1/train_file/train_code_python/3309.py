def solution():
    """Aubriella is pouring water into a 50-gallon fish tank at the rate of 1 gallon every 20 seconds. How many more gallons will she have to pour into the tank to fill the tank if she poured water into the fish tank for 6 minutes?"""
    time_in_seconds = 6 * 60
    gallons_poured_per_second = 1 / 20
    total_gallons_poured = time_in_seconds * gallons_poured_per_second
    gallons_left_to_fill = 50 - total_gallons_poured
    result = gallons_left_to_fill
    return result

print(solution())