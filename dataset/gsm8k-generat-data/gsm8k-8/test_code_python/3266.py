def solution():
    # Calculate the total number of feathers on the goose
    goose_feather_count = 3600

    # Calculate the total weight of all the feathers on the goose in pounds
    goose_feather_weight = goose_feather_count / 300

    # Calculate the number of feathers Miranda can stuff into one pillow
    pillow_feather_weight = 2

    # Calculate the maximum number of pillows Miranda can stuff with the goose feathers
    max_pillows = goose_feather_weight // pillow_feather_weight

    result = max_pillows
    return result

print(solution())