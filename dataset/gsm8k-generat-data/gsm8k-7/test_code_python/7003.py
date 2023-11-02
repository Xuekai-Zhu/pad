def solution():
    num_red_packs = 3
    num_yellow_packs = 10
    num_green_packs = 8
    balls_per_pack = 19

    # Calculate the total number of balls for each color
    red_balls = num_red_packs * balls_per_pack
    yellow_balls = num_yellow_packs * balls_per_pack
    green_balls = num_green_packs * balls_per_pack

    # Calculate the total number of balls Julia bought
    total_balls = red_balls + yellow_balls + green_balls
    result = total_balls
    return result

print(solution())