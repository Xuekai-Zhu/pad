def solution():
    # Calculate the total number of marbles
    total_marbles = 14 + 20 + 19 + 7

    # Calculate how many marbles each friend should have
    per_friend_marbles = total_marbles // 4

    # Return the result
    return per_friend_marbles

print(solution())