def solution():
    # Determine the length of the orange car
    orange_car_length = 1/3.5 * yellow_bus_length

    # Determine the length of the red bus
    red_bus_length = 4 * orange_car_length

    # Determine the visible length of the red bus from the yellow bus
    visible_red_bus_length = red_bus_length - yellow_bus_length

    # Check if the visible length of the red bus is less than or equal to its total length
    if visible_red_bus_length <= 48:
        result = visible_red_bus_length
    else:
        result = "Error: visible length is greater than total length"
    return result

print(solution())