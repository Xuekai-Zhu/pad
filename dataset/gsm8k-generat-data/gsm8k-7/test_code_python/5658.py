def solution():
    dilan_marbles = 14
    martha_marbles = 20
    phillip_marbles = 19
    veronica_marbles = 7

    # Calculate the total number of marbles
    total_marbles = dilan_marbles + martha_marbles + phillip_marbles + veronica_marbles

    # Calculate the number of marbles each friend should have
    num_friends = 4
    marbles_per_friend = total_marbles // num_friends

    result = marbles_per_friend
    return result

print(solution())