def solution():
    """When Pogo, the four-legged martian, walks across the soft Martian soil, it leaves 4 footprints every meter. But Grimzi, the three-legged Plutonian, leaves only 3 footprints in the soft sands of Pluto for every 6 meters it walks. If Pogo travels 6000 meters across the soil of Mars, and Grimzi travels for 6000 meters across the fine sands of Pluto, what is the combined total number of footprints the two creatures will leave on the surfaces of their respective planets?"""
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