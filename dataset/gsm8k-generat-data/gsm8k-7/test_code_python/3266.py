def solution():
    feathers_per_pound = 300
    pounds_per_pillow = 2
    total_feathers = 3600

    # Calculate the total number of pounds of feathers from the goose
    total_pounds = total_feathers / feathers_per_pound

    # Calculate the total number of pillows Miranda can stuff
    num_pillows = total_pounds / pounds_per_pillow
    result = num_pillows
    return result

print(solution())