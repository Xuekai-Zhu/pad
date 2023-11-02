def solution():
    rings_per_play = 5
    play_cost = 1
    points_for_red_bucket = 2
    points_for_green_bucket = 3
    total_points = (rings_per_play * (points_for_red_bucket + points_for_green_bucket)) - play_cost
    result = total_points
    return result

print(solution())