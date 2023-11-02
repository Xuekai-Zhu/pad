def solution():
    """Percius has a collection of marbles. 40% of them are clear. 20% are black, and the remainder are all the other colors. A friend of his asks if he can take five marbles. On average, how many marbles of other colors will his friend end up getting?"""
    total_marbles = 100 # assume Percius has 100 marbles
    clear_marbles = 0.4 * total_marbles
    black_marbles = 0.2 * total_marbles
    other_color_marbles = total_marbles - clear_marbles - black_marbles
    friend_picks = 5
    other_color_average = other_color_marbles / (total_marbles - friend_picks)
    result = other_color_average * friend_picks
    return result

print(solution())