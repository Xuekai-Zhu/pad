def solution():
    cubs_third = 2
    cubs_fifth = 1
    cubs_eighth = 2
    cubs_total = cubs_third + cubs_fifth + cubs_eighth
    cards_second = 1
    cards_fifth = 1
    cards_total = cards_second + cards_fifth
    cubs_score = cubs_total - cards_total
    result = cubs_score
    return result

print(solution())