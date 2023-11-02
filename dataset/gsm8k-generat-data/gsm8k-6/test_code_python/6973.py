def solution():
    # Calculate the amount of water required to fill the tank to 3/4 of its capacity
    water_required = 0.75 * 4000  # 3/4 of 4000 gallons

    # Calculate the time it will take to fill the tank to 3/4 of its capacity
    time_taken = water_required / 10  # 10 gallons per hour

    result = time_taken
    return result

print(solution())