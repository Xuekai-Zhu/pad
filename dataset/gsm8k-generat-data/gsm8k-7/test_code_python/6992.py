def solution():
    money = 3
    red_buckets = 4
    green_buckets = 5
    cost_per_play = 1
    rings_per_play = 5

    # Calculate the total number of plays Tiffany can make
    total_plays = money // cost_per_play

    # Calculate the total number of rings Tiffany has left after the first two games
    total_rings_left = total_plays * rings_per_play - (red_buckets + green_buckets)

    # Calculate the maximum number of red buckets Tiffany can get with the remaining rings
    max_red_buckets = total_rings_left // 2

    # Calculate the maximum number of green buckets Tiffany can get with the remaining rings
    max_green_buckets = total_rings_left // 3

    # Calculate the total number of points Tiffany can get in all three games
    total_points = (red_buckets + max_red_buckets) * 2 + (green_buckets + max_green_buckets) * 3
    result = total_points
    return result

print(solution())