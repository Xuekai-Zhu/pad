def solution():
    feathers_per_pound = 300  # A pound of goose feathers is approximately 300 feathers
    feathers_per_pillow = 2 * feathers_per_pound  # Miranda needs 2 pounds of feathers for each pillow
    total_feathers = 3600  # Miranda's goose has approximately 3600 feathers

    # Calculate the total number of pillows Miranda can stuff with the goose feathers
    total_pillows = total_feathers / feathers_per_pillow
    result = total_pillows
    return result

print(solution())