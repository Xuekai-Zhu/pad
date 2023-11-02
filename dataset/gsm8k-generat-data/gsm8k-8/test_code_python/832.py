def solution():
    # Calculate the total amount of air needed for all balloons
    total_air = 1000 * 10

    # Calculate the number of tanks needed to hold the total air
    tanks = total_air / 500

    # Round up to the nearest whole number
    tanks = math.ceil(tanks)

    result = tanks
    return result

print(solution())