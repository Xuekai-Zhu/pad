def solution():
    """Grady has 20 red numbered cubes and 15 blue numbered cubes. He gives his friend Gage 2/5 of his red numbered cubes and 1/3 of the blue numbered cubes. If Gage had 10 red numbered cubes and 12 blue numbered cubes, find the total number of cubes Gage has."""
    grady_red_cubes = 20
    grady_blue_cubes = 15
    gage_red_cubes = 10
    gage_blue_cubes = 12
    red_cubes_given = (2/5) * grady_red_cubes
    blue_cubes_given = (1/3) * grady_blue_cubes
    # We can set up two equations using the given information:
    # 1) Gage has 10 red cubes: gage_red_cubes = grady_red_cubes - red_cubes_given
    # 2) Gage has 12 blue cubes: gage_blue_cubes = grady_blue_cubes - blue_cubes_given
    # Solving these equations for grady_red_cubes and grady_blue_cubes, we find:
    grady_red_cubes = (5/3) * (gage_red_cubes - 10)
    grady_blue_cubes = 3 * (gage_blue_cubes - 12)
    total_cubes = gage_red_cubes + gage_blue_cubes + grady_red_cubes + grady_blue_cubes
    result = total_cubes
    return result

print(solution())