def solution():
    num_red_packs = 7
    num_yellow_packs = 6
    balls_per_pack = 18

    # Calculate the total number of red bouncy balls
    total_red_balls = num_red_packs * balls_per_pack

    # Calculate the total number of yellow bouncy balls
    total_yellow_balls = num_yellow_packs * balls_per_pack

    # Calculate the difference in number of red and yellow bouncy balls
    diff = total_red_balls - total_yellow_balls
    result = diff
    return result

print(solution())