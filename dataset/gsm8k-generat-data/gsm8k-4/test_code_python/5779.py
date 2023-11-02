def solution():
    """Betty has 3 red beads for every 2 blue beads that she has. How many blue beads does Betty have if she has 30 red beads?"""
    # Define the ratio of red beads to blue beads
    ratio_red_blue = 3/2

    # Define the number of red beads
    red_beads = 30

    # Calculate the number of blue beads
    blue_beads = red_beads / ratio_red_blue * 2

    result = blue_beads
    return result

print(solution())