def solution():
    """Percius has a collection of marbles. 40% of them are clear. 20% are black, and the remainder are all the other colors. A friend of his asks if he can take five marbles. On average, how many marbles of other colors will his friend end up getting?"""
    total_marbles = 100
    clear_marbles = 40
    black_marbles = 20
    other_marbles = total_marbles - clear_marbles - black_marbles
    friend_marbles = 5
    other_marbles_prob = other_marbles / (total_marbles - friend_marbles)
    result = other_marbles_prob * friend_marbles
    return result

print(solution())