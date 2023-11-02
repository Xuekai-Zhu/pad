def solution():
    # Define the number of packs of each color that Julia bought
    red_packs = 3
    yellow_packs = 10
    green_packs = 8

    # Define the number of balls in each pack
    balls_per_pack = 19

    # Calculate the total number of balls Julia bought
    total_balls = (red_packs + yellow_packs + green_packs) * balls_per_pack
    result = total_balls
    return result

print(solution())