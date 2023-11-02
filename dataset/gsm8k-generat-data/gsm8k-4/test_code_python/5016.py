def solution():
    """Percius has a collection of marbles. 40% of them are clear. 20% are black, and the remainder are all the other colors. A friend of his asks if he can take five marbles. On average, how many marbles of other colors will his friend end up getting?"""
    # Define the proportions of each color of marbles
    clear_proportion = 0.4
    black_proportion = 0.2
    other_proportion = 1 - clear_proportion - black_proportion

    # Define the total number of marbles
    total_marbles = 100

    # Define the number of marbles that the friend will take
    friend_marbles = 5

    # Calculate the expected number of marbles of other colors that the friend will get
    other_marbles = friend_marbles * other_proportion

    # return the result
    result = other_marbles
    return result

print(solution())