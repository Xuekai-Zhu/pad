def solution():
    """Miranda is stuffing feather pillows. She needs two pounds of feathers for each pillow. A pound of goose feathers is approximately 300 feathers. Her goose has approximately 3600 feathers. How many pillows can she stuff after she plucks the goose?"""
    # Define the number of feathers needed per pillow and the number of feathers per pound
    FEATHERS_PER_PILLOW = 2 * 300

    # Calculate the number of pillows that can be stuffed with the feathers from the goose
    feathers_total = 3600
    pillows = feathers_total // FEATHERS_PER_PILLOW

    # Display the number of pillows that can be stuffed
    result = pillows
    return result

print(solution())