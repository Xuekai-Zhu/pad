def solution():
    # Define the number of packs and bouncy balls in each pack
    red_packs = 5
    yellow_packs = 4
    balls_per_pack = 18

    # Calculate the total number of bouncy balls bought
    total_red_balls = red_packs * balls_per_pack
    total_yellow_balls = yellow_packs * balls_per_pack

    # Calculate the difference between the number of red and yellow bouncy balls
    difference = total_red_balls - total_yellow_balls
    result = difference
    return result

print(solution())