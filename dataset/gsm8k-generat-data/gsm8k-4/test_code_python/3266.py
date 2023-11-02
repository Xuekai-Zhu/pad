def solution():
    """Miranda is stuffing feather pillows. She needs two pounds of feathers for each pillow. A pound of goose feathers is approximately 300 feathers. Her goose has approximately 3600 feathers. How many pillows can she stuff after she plucks the goose?"""
    # Define the number of feathers in a pound and the total number of feathers on the goose
    feathers_per_pound = 300
    total_feathers = 3600

    # Calculate the total number of pounds of feathers on the goose
    total_pounds = total_feathers / feathers_per_pound

    # Calculate the total number of pillows that can be stuffed
    pillows = total_pounds / 2

    result = round(pillows)
    return result

print(solution())