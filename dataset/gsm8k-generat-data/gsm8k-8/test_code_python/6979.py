def solution():
    # Define the length of the red bus and length of the orange car in terms of the length of a yellow bus
    yellow_bus_length = 1
    orange_car_length = 0.25 * yellow_bus_length
    red_bus_length = 4 * orange_car_length

    # Calculate the proportion of the red bus length that the yellow bus driver can see
    visible_proportion = yellow_bus_length / (yellow_bus_length + red_bus_length)

    # Calculate the length of the red bus visible to the yellow bus driver
    visible_length = visible_proportion * 48

    result = visible_length
    return result

print(solution())