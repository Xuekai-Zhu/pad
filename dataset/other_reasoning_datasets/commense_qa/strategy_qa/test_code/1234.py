def solution():
    honey_badger_shoulder_height = 23
    honey_badger_body_length = 77
    oven_width = 25
    oven_height = 16
    oven_depth = 16
    # Check if the honey badger fits inside the oven in all dimensions
    if honey_badger_shoulder_height <= oven_height and honey_badger_body_length <= oven_width and honey_badger_body_length <= oven_depth:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())