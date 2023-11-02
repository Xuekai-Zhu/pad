def solution():
    """Grady has 20 red numbered cubes and 15 blue numbered cubes. He gives his friend Gage 2/5 of his red numbered cubes and 1/3 of the blue numbered cubes. If Gage had 10 red numbered cubes and 12 blue numbered cubes, find the total number of cubes Gage has?"""
    # Define the initial number of red and blue cubes Grady has
    initial_red = 20
    initial_blue = 15

    # Calculate the number of cubes Grady gives to Gage
    gage_red = 2/5 * initial_red
    gage_blue = 1/3 * initial_blue

    # Calculate the final number of red and blue cubes Gage has
    final_red = 10 + gage_red
    final_blue = 12 + gage_blue

    # Calculate the total number of cubes Gage has
    total_cubes = final_red + final_blue

    # Display the total number of cubes Gage has
    result = total_cubes
    return result

print(solution())