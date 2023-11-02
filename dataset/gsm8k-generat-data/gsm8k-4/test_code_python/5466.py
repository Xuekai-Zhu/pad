def solution():
    """Grady has 20 red numbered cubes and 15 blue numbered cubes. He gives his friend Gage 2/5 of his red numbered cubes and 1/3 of the blue numbered cubes. If Gage had 10 red numbered cubes and 12 blue numbered cubes, find the total number of cubes Gage has?"""
    # Define the initial number of red and blue cubes Grady has
    initial_red_cubes = 20
    initial_blue_cubes = 15

    # Define the number of red and blue cubes Gage gets
    gage_red_cubes = (2/5) * initial_red_cubes
    gage_blue_cubes = (1/3) * initial_blue_cubes

    # Calculate the remaining red and blue cubes after giving some to Gage
    remaining_red_cubes = initial_red_cubes - gage_red_cubes
    remaining_blue_cubes = initial_blue_cubes - gage_blue_cubes

    # Check that Gage has the correct number of red and blue cubes
    if gage_red_cubes == 10 and gage_blue_cubes == 12:
        # Calculate the total number of cubes Gage has
        total_cubes = gage_red_cubes + gage_blue_cubes + remaining_red_cubes + remaining_blue_cubes

        result = total_cubes
    else:
        result = "Gage does not have the correct number of cubes."

    return result

print(solution())