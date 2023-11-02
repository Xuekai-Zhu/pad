def solution():
    money_to_play = 3  # Tiffany has $3 to play the game
    cost_per_play = 1  # Each play costs $1
    rings_per_play = 5  # Tiffany gets 5 rings per play
    total_plays = (money_to_play // cost_per_play) * rings_per_play  # Tiffany can play this many times with her money
    red_buckets = 4  # Tiffany has already gotten 4 red buckets
    green_buckets = 5  # Tiffany has already gotten 5 green buckets
    total_points = (red_buckets * 2) + (green_buckets * 3)  # Tiffany has this many points already
    remaining_plays = total_plays - (red_buckets + green_buckets)  # Tiffany has this many plays remaining

    # Calculate the maximum possible points Tiffany can get with the remaining plays
    remaining_red_buckets = remaining_plays // 2
    remaining_green_buckets = remaining_plays // 3
    possible_points = (remaining_red_buckets * 2) + (remaining_green_buckets * 3)

    # Add the possible points to the total points
    total_points += possible_points
    result = total_points
    return result

print(solution())