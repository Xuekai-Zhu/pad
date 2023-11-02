def solution():
    """The length of a red bus is four times the length of an orange car. The length of the orange car is also 3.5 times shorter than the length of a yellow bus. If the yellow bus and red bus are sitting next to each other, what length of the red bus may the yellow bus driver see if the red bus is 48 feet long?"""
    # Define the length of the red bus
    red_bus_length = 48

    # Calculate the length of the orange car
    orange_car_length = red_bus_length / 4

    # Calculate the length of the yellow bus
    yellow_bus_length = orange_car_length / (1 - 3.5)

    # Calculate the length of the portion of the red bus visible to the yellow bus driver
    visible_length = red_bus_length - yellow_bus_length

    # Display the visible length of the red bus
    result = visible_length
    return result

print(solution())