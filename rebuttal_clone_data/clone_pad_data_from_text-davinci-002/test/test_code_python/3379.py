def solution():
    racers = 100
    eliminated_1 = 10
    left_1 = racers - eliminated_1
    eliminated_2 = left_1 / 3
    left_2 = left_1 - eliminated_2
    eliminated_3 = left_2 / 2
    left_3 = left_2 - eliminated_3
    result = left_3
    return result

print(solution())