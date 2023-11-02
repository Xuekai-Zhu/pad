def solution():
    # Calculate the total amount of time in seconds Aubriella pours the water
    time_in_seconds = 6 * 60

    # Calculate the number of gallons of water Aubriella poured in the tank
    gallons_poured = (time_in_seconds / 20)

    # Calculate the amount of water needed to fill the tank
    water_needed = 50 - gallons_poured

    result = water_needed
    return result

print(solution())