def solution():
    # Find the number of red cubes Grady gave to Gage
    red_cubes_given = (2/5) * 20  # Grady gave 2/5 of his total red cubes
    # Find the number of blue cubes Grady gave to Gage
    blue_cubes_given = (1/3) * 15  # Grady gave 1/3 of his total blue cubes
    # Calculate the total number of cubes Gage has
    total_red_cubes = red_cubes_given + 10  # Gage had 10 red cubes before receiving from Grady
    total_blue_cubes = blue_cubes_given + 12  # Gage had 12 blue cubes before receiving from Grady
    total_cubes = total_red_cubes + total_blue_cubes
    result = total_cubes
    return result

print(solution())