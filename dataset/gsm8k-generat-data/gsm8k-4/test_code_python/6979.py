def solution():
    """The length of a red bus is four times the length of an orange car. 
    The length of the orange car is also 3.5 times shorter than the length of a yellow bus. 
    If the yellow bus and red bus are sitting next to each other, what length of the red bus may the yellow bus driver see if the red bus is 48 feet long?"""
    
    # Calculate the length of the orange car
    orange_car_length = 1/3.5 * 48
    
    # Calculate the length of the red bus
    red_bus_length = 4 * orange_car_length
    
    # Calculate the total length of the buses
    total_length = red_bus_length + 48
    
    # Calculate the visible length of the red bus from the yellow bus driver's perspective
    visible_length = total_length - 48
    
    result = visible_length
    return result

print(solution())