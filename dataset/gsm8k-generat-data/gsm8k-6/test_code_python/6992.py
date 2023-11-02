def solution():
    # Calculate the total number of points Tiffany can get for all three games
    total_plays = 3  # Tiffany will play three games until her money runs out
    total_rings = total_plays * 5  # Tiffany gets 5 rings per play

    # Calculate the total number of red and green buckets in all three games
    total_red_buckets = 4 * total_plays  # Tiffany got 4 red buckets in two games, so she can get 4 more in the third game
    total_green_buckets = 5 * total_plays  # Tiffany got 5 green buckets in two games, so she can get 5 more in the third game

    # Calculate the total number of points Tiffany can get for all three games
    total_points = (total_red_buckets * 2) + (total_green_buckets * 3)  # Tiffany gets 2 points for every red bucket and 3 points for every green bucket

    # Calculate the total cost of all three games
    total_cost = total_plays

    # Calculate how many games Tiffany can play with her remaining money
    remaining_money = 3 - total_cost
    remaining_plays = int(remaining_money / 1)

    # Calculate the total number of rings Tiffany has left
    remaining_rings = total_rings - (total_plays * 5)

    # Calculate the total number of red and green buckets Tiffany can get in the remaining games
    remaining_red_buckets = remaining_rings  # Tiffany will get 1 red bucket for every ring she has left
    remaining_green_buckets = 0  # Tiffany will not have enough rings to get any green buckets

    # Calculate the total number of points Tiffany can get in the remaining games
    remaining_points = (remaining_red_buckets * 2) + (remaining_green_buckets * 3)

    # Add the total points from all three games
    total_points += remaining_points

    result = total_points
    return result

print(solution())