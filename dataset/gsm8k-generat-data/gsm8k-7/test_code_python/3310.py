def solution():
    tank_capacity = 50  # gallons
    rate = 1  # gallon per 20 seconds
    time = 6 * 60  # in seconds

    # Calculate the total number of gallons poured in 6 minutes
    num_gallons_poured = (time / 20) * rate

    # Calculate how much more gallons Aubriella needs to pour to fill the tank
    remaining_gallons = tank_capacity - num_gallons_poured
    result = remaining_gallons
    return result

print(solution())