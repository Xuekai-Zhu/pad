def solution():
    # Calculate the total amount of water that can be carried in 20 cans at three quarters capacity
    total_water = 20 * 8 * 0.75

    # Calculate the rate of filling in gallons per hour
    rate = total_water / 3

    # Calculate the total amount of water required to fill 25 cans to full capacity
    total_required = 25 * 8

    # Calculate the time taken to fill 25 cans to full capacity
    time = total_required / rate
    result = time
    return result

print(solution())