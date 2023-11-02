def solution():
    # Calculate the number of hikes each person has gone on
    camila_hikes = 7
    amanda_hikes = 8 * camila_hikes
    steven_hikes = amanda_hikes + 15

    # Calculate how many more hikes Camila needs to go on to match Steven's total
    hikes_needed = steven_hikes - camila_hikes

    # Calculate how many weeks it will take Camila to go on the remaining hikes
    weeks_needed = hikes_needed / 4

    # Round up to the nearest whole number of weeks
    weeks_needed = math.ceil(weeks_needed)
    result = weeks_needed
    return result

print(solution())