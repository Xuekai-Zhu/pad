def solution():
    red_cubes = 20
    blue_cubes = 15

    # Grady gives Gage 2/5 of his red cubes
    gage_red_cubes = int(2/5 * red_cubes)
    remaining_red_cubes = red_cubes - gage_red_cubes

    # Grady gives Gage 1/3 of his blue cubes
    gage_blue_cubes = int(1/3 * blue_cubes)
    remaining_blue_cubes = blue_cubes - gage_blue_cubes

    # Check if Gage has the given number of red and blue cubes
    if gage_red_cubes == 10 and gage_blue_cubes == 12:
        total_cubes = gage_red_cubes + gage_blue_cubes + remaining_red_cubes + remaining_blue_cubes
        result = total_cubes
    else:
        result = "Error: Gage doesn't have the given number of cubes"

    return result

print(solution())