def solution():
    swims_camden = 16
    swims_susannah = 24
    total_swims = swims_camden + swims_susannah
    swims_per_week = total_swims / 4
    difference = swims_susannah - swims_camden
    result = difference / swims_per_week
    return result

print(solution())