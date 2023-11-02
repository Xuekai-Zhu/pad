def solution():
    num_red_cubes = 20
    num_blue_cubes = 15
    red_portion = 2/5
    blue_portion = 1/3
    gage_red_cubes = 10
    gage_blue_cubes = 12

    # Calculate how many red and blue cubes Grady gave to Gage
    num_given_red_cubes = num_red_cubes * red_portion
    num_given_blue_cubes = num_blue_cubes * blue_portion

    # Calculate how many red and blue cubes Gage received from Grady
    gage_red_cubes_received = gage_red_cubes + num_given_red_cubes
    gage_blue_cubes_received = gage_blue_cubes + num_given_blue_cubes

    # Calculate the total number of cubes Gage has
    total_cubes = gage_red_cubes_received + gage_blue_cubes_received
    result = total_cubes
    return result

print(solution())