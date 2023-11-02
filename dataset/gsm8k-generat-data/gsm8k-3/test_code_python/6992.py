def solution():
    """Tiffany attends the carnival and her mother gives her $3 to play on a ring toss game. For every red bucket she tosses a ring into she gets 2 points. For every green bucket she gets three points. She gets zero points for a miss. Every play costs her $1 and she gets 5 rings per play. She's played two games and already gotten 4 red buckets and 5 green buckets. If she plays until her money runs out, what is the most total points she can get for all three games?"""
    # Define the number of points awarded for each bucket
    RED_POINTS = 2
    GREEN_POINTS = 3

    # Define the cost per play and number of rings per play
    COST_PER_PLAY = 1
    RINGS_PER_PLAY = 5

    # Define the starting amount of money
    money = 3

    # Define the starting number of buckets
    red_buckets = 4
    green_buckets = 5

    # Calculate the number of plays possible with the starting money
    plays = money // COST_PER_PLAY

    # Calculate the number of rings possible with the number of plays
    rings = plays * RINGS_PER_PLAY

    # Calculate the number of red buckets and green buckets possible with the rings
    red_buckets_possible = rings // RED_POINTS
    green_buckets_possible = rings // GREEN_POINTS

    # Calculate the maximum number of points possible with the remaining money
    remaining_money = money - plays * COST_PER_PLAY
    remaining_rings = remaining_money // COST_PER_PLAY * RINGS_PER_PLAY
    remaining_red_buckets_possible = remaining_rings // RED_POINTS
    remaining_green_buckets_possible = remaining_rings // GREEN_POINTS
    total_red_buckets = red_buckets + red_buckets_possible + remaining_red_buckets_possible
    total_green_buckets = green_buckets + green_buckets_possible + remaining_green_buckets_possible
    total_points = total_red_buckets * RED_POINTS + total_green_buckets * GREEN_POINTS

    # Display the total points
    result = total_points
    return result

print(solution())