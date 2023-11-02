def solution():
    """Betty has 3 red beads for every 2 blue beads that she has. How many blue beads does Betty have if she has 30 red beads?"""
    red_beads = 30
    red_blue_ratio = 3/2
    blue_beads = (red_beads / red_blue_ratio) * (1/2)
    result = blue_beads
    return result

print(solution())