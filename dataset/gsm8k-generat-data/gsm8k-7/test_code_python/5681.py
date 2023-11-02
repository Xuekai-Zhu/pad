def solution():
    red_balls_per_pack = 18
    yellow_balls_per_pack = 18
    num_red_packs = 5
    num_yellow_packs = 4

    # Calculate the total number of red balls
    total_red_balls = num_red_packs * red_balls_per_pack

    # Calculate the total number of yellow balls
    total_yellow_balls = num_yellow_packs * yellow_balls_per_pack

    # Calculate the difference between the total number of red and yellow balls
    difference = total_red_balls - total_yellow_balls
    result = difference
    return result

print(solution())