def solution():
    """Janelle had 26 green marbles. Then she bought 6 bags of blue marbles. There were 10 marbles in each bag. She created a gift of 6 green marbles and 8 blue marbles and gave it to a friend. How many marbles does Janelle have now?"""
    initial_green_marbles = 26
    blue_marbles_per_bag = 10
    total_blue_marbles = 6 * blue_marbles_per_bag
    green_marbles_given_away = 6
    blue_marbles_given_away = 8
    remaining_green_marbles = initial_green_marbles - green_marbles_given_away
    remaining_blue_marbles = total_blue_marbles - blue_marbles_given_away
    total_marbles = remaining_green_marbles + remaining_blue_marbles
    result = total_marbles
    return result

print(solution())