def solution():
    pogo_footprints_per_meter = 4  # Pogo leaves 4 footprints per meter on Mars
    pogo_distance = 6000  # Pogo travels 6000 meters on Mars

    grimzi_footprints_per_6m = 3  # Grimzi leaves 3 footprints for every 6 meters on Pluto
    grimzi_distance = 6000  # Grimzi travels 6000 meters on Pluto

    # Calculate the total number of footprints Pogo leaves on Mars
    pogo_footprints = pogo_footprints_per_meter * pogo_distance

    # Calculate the total number of footprints Grimzi leaves on Pluto
    grimzi_footprints = (grimzi_footprints_per_6m / 6) * grimzi_distance

    # Calculate the combined total number of footprints on both planets
    total_footprints = pogo_footprints + grimzi_footprints
    result = total_footprints
    return result

print(solution())