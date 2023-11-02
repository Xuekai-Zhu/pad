def solution():
    """Miranda is stuffing feather pillows. She needs two pounds of feathers for each pillow. A pound of goose feathers is approximately 300 feathers. Her goose has approximately 3600 feathers. How many pillows can she stuff after she plucks the goose?"""
    feathers_per_pound = 300
    goose_feathers = 3600
    total_feathers = goose_feathers
    total_pillow_feathers = 2 * feathers_per_pound
    pillows = total_feathers // total_pillow_feathers
    result = pillows
    return result

print(solution())