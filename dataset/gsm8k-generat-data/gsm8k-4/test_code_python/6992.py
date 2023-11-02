def solution():
    """Tiffany attends the carnival and her mother gives her $3 to play on a ring toss game. For every red bucket she tosses a ring into she gets 2 points. For every green bucket she gets three points. She gets zero points for a miss. Every play costs her $1 and she gets 5 rings per play. She's played two games and already gotten 4 red buckets and 5 green buckets. If she plays until her money runs out, what is the most total points she can get for all three games?"""
    # Define the initial amount of money and the cost per play
    INITIAL_MONEY = 3
    COST_PER_PLAY = 1

    # Define the number of rings per play and the points awarded for each bucket
    RINGS_PER_PLAY = 5
    RED_POINTS = 2
    GREEN_POINTS = 3

    # Calculate the number of plays available based on the initial amount of money and the cost per play
    plays_available = INITIAL_MONEY // COST_PER_PLAY

    # Calculate the total number of rings she has left
    rings_left = plays_available * RINGS_PER_PLAY

    # Calculate the total number of buckets she has left to toss into
    total_buckets = 3 * 2  # 2 games already played, plus 1 game to be played with remaining money

    # Calculate the total number of points she can earn with the remaining buckets and rings
    red_buckets_left = 4
    green_buckets_left = 5
    red_points_left = red_buckets_left * RED_POINTS
    green_points_left = green_buckets_left * GREEN_POINTS
    total_points = red_points_left + green_points_left

    # Calculate the maximum number of plays she can have with the remaining money and rings
    max_plays_with_remaining_money_and_rings = rings_left // RINGS_PER_PLAY

    # Calculate the maximum number of points she can earn with the remaining money and rings
    max_red_buckets = red_buckets_left + (max_plays_with_remaining_money_and_rings * 2) # Every missed throw, one red bucket becomes available to her
    max_green_buckets = green_buckets_left + (max_plays_with_remaining_money_and_rings * 3) # Every missed throw, one green bucket becomes available to her
    max_points_remaining = (max_red_buckets * RED_POINTS) + (max_green_buckets * GREEN_POINTS)

    # Calculate the total maximum points she can earn for all three games
    total_max_points = total_points + max_points_remaining

    result = total_max_points
    return result

print(solution())