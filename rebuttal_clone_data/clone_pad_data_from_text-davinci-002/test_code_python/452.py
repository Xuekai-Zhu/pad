def solution():
    marbles = 6
    marbles_doubled = marbles * 2
    marbles_given_back = (marbles_doubled / 2) + 1
    marbles_left = marbles_doubled - marbles_given_back
    result = marbles_left
    return result

print(solution())