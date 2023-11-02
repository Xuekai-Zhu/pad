def solution():
    brown_rice_expensive = True
    store_rice_pudding_white = True
    brown_rice_light_brown_when_cooked = True
    
    if not brown_rice_expensive and store_rice_pudding_white:
        result = "no"
    elif brown_rice_light_brown_when_cooked and store_rice_pudding_white:
        result = "some"
    else:
        result = "unknown"
    return result

print(solution())