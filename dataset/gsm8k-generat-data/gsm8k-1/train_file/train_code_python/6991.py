def solution():
    """Tiffany attends the carnival and her mother gives her $3 to play on a ring toss game. For every red bucket she tosses a ring into she gets 2 points. For every green bucket she gets three points. She gets zero points for a miss. Every play costs her $1 and she gets 5 rings per play. She's played two games and already gotten 4 red buckets and 5 green buckets. If she plays until her money runs out, what is the most total points she can get for all three games?"""
    money = 3
    cost_per_play = 1
    rings_per_play = 5
    total_plays = money // cost_per_play
    total_rings = total_plays * rings_per_play
    red_buckets = 4
    green_buckets = 5
    
    # calculating points from first two games
    points_from_red_buckets = red_buckets * 2 * 2
    points_from_green_buckets = green_buckets * 3 * 2
    total_points = points_from_red_buckets + points_from_green_buckets
    
    # calculating potential points from third game
    remaining_rings = total_rings - (red_buckets + green_buckets) * 2
    remaining_plays = remaining_rings // rings_per_play
    potential_red_buckets = remaining_plays // 2
    potential_green_buckets = remaining_plays - (potential_red_buckets * 2)
    potential_points = (potential_red_buckets * 2 * 2) + (potential_green_buckets * 3)
    
    # returning total points
    result = total_points + potential_points
    return result

print(solution())