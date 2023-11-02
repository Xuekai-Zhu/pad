def solution():
    # Calculate the total amount of water filled in 20 eight gallon cans
    water_filled = 20 * 8 * 0.75

    # Calculate the rate of filling (in gallons per hour)
    rate = water_filled / 3

    # Calculate the total amount of water required for 25 cans filled to full capacity
    total_water = 25 * 8

    # Calculate the time it will take to fill the 25 cans (in hours)
    time = total_water / rate
    result = time
    return result

print(solution())