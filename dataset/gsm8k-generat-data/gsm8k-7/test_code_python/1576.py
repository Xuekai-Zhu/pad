def solution():
    pogo_footprints_per_meter = 4
    pogo_distance = 6000

    grimzi_footprints_per_6_meters = 3
    grimzi_distance = 6000

    # Calculate the total number of footprints left by Pogo on Mars
    total_pogo_footprints = pogo_footprints_per_meter * pogo_distance

    # Calculate the total number of footprints left by Grimzi on Pluto
    total_grimzi_footprints = (grimzi_footprints_per_6_meters / 6) * grimzi_distance

    # Calculate the combined total number of footprints left by both creatures
    combined_total_footprints = total_pogo_footprints + total_grimzi_footprints
    result = combined_total_footprints
    return result

print(solution())