def solution():
    # Define points for each bucket type
    red_points = 2
    green_points = 3

    # Define number of rings thrown per game and cost per game
    rings_per_game = 5
    cost_per_game = 1

    # Define remaining money after first two games
    remaining_money = 1

    # Calculate total points for first two games
    total_points = (4 * red_points) + (5 * green_points)

    # Calculate remaining number of games
    remaining_games = remaining_money // cost_per_game

    # Calculate remaining rings
    remaining_rings = remaining_games * rings_per_game

    # Calculate remaining points
    remaining_red_buckets = remaining_rings // 2
    remaining_green_buckets = remaining_rings - remaining_red_buckets
    remaining_points = (remaining_red_buckets * red_points) + (remaining_green_buckets * green_points)

    # Calculate total points for all three games
    total_points += remaining_points

    result = total_points
    return result

print(solution())