def solution():
    # Calculate the number of footprints left by Pogo on Mars
    pogo_footprints = 4 * 6000  # Pogo leaves 4 footprints every meter

    # Calculate the number of footprints left by Grimzi on Pluto
    grimzi_footprints = (3/6) * 6000 * 3  # Grimzi leaves 3 footprints every 6 meters, and has 3 legs

    # Calculate the total number of footprints left by both creatures
    total_footprints = pogo_footprints + grimzi_footprints
    result = total_footprints
    return result

print(solution())