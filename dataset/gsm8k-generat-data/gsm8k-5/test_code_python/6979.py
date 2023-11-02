def solution():
    length_yellow_bus = 48  # The length of the yellow bus is given as 48 feet
    length_orange_car = length_yellow_bus / (3.5 * 4)  # The length of the orange car is 3.5 times shorter than the length of the yellow bus and 4 times shorter than the length of the red bus
    length_red_bus_seen = length_orange_car * 4  # The length of the red bus seen by the yellow bus driver is 4 times the length of the orange car

    result = length_red_bus_seen
    return result

print(solution())