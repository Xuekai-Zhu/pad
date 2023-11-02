def solution():
    red_packs = 3  # Julia bought 3 packs of red balls
    yellow_packs = 10  # Julia bought 10 packs of yellow balls
    green_packs = 8  # Julia bought 8 packs of green balls
    balls_per_pack = 19  # Each pack contains 19 balls

    # Calculate the total number of balls Julia bought
    total_balls = (red_packs + yellow_packs + green_packs) * balls_per_pack
    result = total_balls
    return result

print(solution())