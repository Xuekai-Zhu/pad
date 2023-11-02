def solution():
    yeti_weight_range = range(200, 401)
    yeti_height = 6
    andre_height = 7.33 # convert 7'4" to feet
    andre_weight = 529
    if yeti_height < andre_height and max(yeti_weight_range) < andre_weight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())