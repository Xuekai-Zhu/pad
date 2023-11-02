def solution():
    """The length of a red bus is four times the length of an orange car. The length of the orange car is also 3.5 times shorter than the length of a yellow bus. If the yellow bus and red bus are sitting next to each other, what length of the red bus may the yellow bus driver see if the red bus is 48 feet long?"""
    yellow_bus_length = 4 * (48 / 4) / 3.5
    visible_red_bus_length = 48 - yellow_bus_length
    result = visible_red_bus_length
    return result

print(solution())