def solution():
    # Calculate the number of red cubes Grady gave to Gage
    red_cubes_given = (2/5) * 20
    # Calculate the total number of remaining red cubes Grady has
    red_cubes_remaining = 20 - red_cubes_given
    # Calculate the number of blue cubes Grady gave to Gage
    blue_cubes_given = (1/3) * 15
    # Calculate the total number of remaining blue cubes Grady has
    blue_cubes_remaining = 15 - blue_cubes_given
    # Calculate the total number of cubes Gage has
    total_cubes = red_cubes_given + blue_cubes_given + 10 + 12
    result = total_cubes
    return result

print(solution())