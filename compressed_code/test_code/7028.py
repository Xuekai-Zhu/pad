def solution():
    
    pogo_fps_per_m = 4
    pogo_distance = 6000
    pogo_total_fps = pogo_fps_per_m * pogo_distance

    grimzi_fps_per_6m = 3
    grimzi_distance = 6000
    grimzi_total_fps = (grimzi_distance / 6) * grimzi_fps_per_6m

    total_footprints = pogo_total_fps + grimzi_total_fps
    result = total_footprints

    return result

print(solution())