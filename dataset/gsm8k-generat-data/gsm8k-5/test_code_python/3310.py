def solution():
    seconds_in_minute = 60  # There are 60 seconds in a minute
    total_time = 6 * seconds_in_minute  # Aubriella poured water into the fish tank for 6 minutes
    rate = 1 / 20  # Aubriella pours water into the fish tank at a rate of 1 gallon every 20 seconds

    # Calculate the total amount of water Aubriella poured into the fish tank during the given time
    total_water_poured = rate * total_time

    # Calculate the amount of water needed to fill the tank
    remaining_water = 50 - total_water_poured
    result = remaining_water
    return result

print(solution())