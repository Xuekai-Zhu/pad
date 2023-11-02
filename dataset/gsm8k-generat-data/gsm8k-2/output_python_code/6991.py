def solution():
    """Tiffany attends the carnival and her mother gives her $3 to play on a ring toss game. For every red bucket she tosses a ring into she gets 2 points. For every green bucket she gets three points. She gets zero points for a miss. Every play costs her $1 and she gets 5 rings per play. She's played two games and already gotten 4 red buckets and 5 green buckets. If she plays until her money runs out, what is the most total points she can get for all three games?"""
    starting_money = 3
    cost_per_game = 1
    rings_per_game = 5
    red_buckets_per_ring = 2
    green_buckets_per_ring = 3
    red_buckets_so_far = 4
    green_buckets_so_far = 5
    total_points = (red_buckets_so_far + green_buckets_so_far) * (red_buckets_per_ring + green_buckets_per_ring)
    remaining_money = starting_money - cost_per_game * 2
    remaining_plays = remaining_money // cost_per_game
    remaining_rings = remaining_plays * rings_per_game
    remaining_red_buckets = remaining_rings * red_buckets_per_ring
    remaining_green_buckets = remaining_rings * green_buckets_per_ring
    total_points += (remaining_red_buckets + remaining_green_buckets)
    result = total_points
    return result

print(solution())