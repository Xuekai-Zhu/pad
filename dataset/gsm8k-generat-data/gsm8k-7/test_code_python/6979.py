def solution():
    red_bus_length = 48
    orange_car_length = red_bus_length / 4
    yellow_bus_length = orange_car_length / (1 - 3.5)

    # Calculate the visible length of the red bus
    visible_red_bus_length = red_bus_length - yellow_bus_length

    result = visible_red_bus_length
    return result

print(solution())