def solution():
    """Miranda is stuffing feather pillows. She needs two pounds of feathers for each pillow. A pound of goose feathers is approximately 300 feathers. Her goose has approximately 3600 feathers. How many pillows can she stuff after she plucks the goose?"""
    feathers_per_pound = 300
    feathers_per_pillow = feathers_per_pound * 2
    total_feathers = 3600
    pillows_stuffed = total_feathers // feathers_per_pillow
    result = pillows_stuffed
    return result

print(solution())