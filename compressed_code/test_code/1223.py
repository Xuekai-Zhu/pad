def solution():
    
    pogo_footprints_per_meter = 4
    pogo_distance = 6000
    pogo_total_footprints = pogo_footprints_per_meter * pogo_distance

    grimzi_footprints_per_meter = 3 / 6
    grimzi_distance = 6000
    grimzi_total_footprints = grimzi_footprints_per_meter * grimzi_distance

    total_footprints = pogo_total_footprints + grimzi_total_footprints
    result = total_footprints
    return result

print(solution())