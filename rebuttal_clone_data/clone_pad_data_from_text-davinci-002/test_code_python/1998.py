def solution():
    marbles = 100
    marbles_kept = 20
    marbles_shared = marbles - marbles_kept
    friends = 5
    marbles_per_friend = marbles_shared // friends
    result = marbles_per_friend
    return result

print(solution())