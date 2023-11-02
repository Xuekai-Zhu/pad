def solution():
    balloons = 1000  # John buys 1000 balloons
    balloon_volume = 10  # Each balloon holds 10 liters of air
    total_volume = balloons * balloon_volume  # Calculate the total volume of air needed
    tank_volume = 500  # John buys 500-liter tanks of gas
    tanks_needed = total_volume // tank_volume  # Round down to get the number of tanks needed
    if total_volume % tank_volume != 0:  # If there is a partial tank needed, add one more to the total
        tanks_needed += 1
    result = tanks_needed
    return result

print(solution())