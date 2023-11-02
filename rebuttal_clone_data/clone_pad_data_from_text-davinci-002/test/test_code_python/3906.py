def solution():
    pits_planted = 80
    pits_sprouted = pits_planted * 0.25
    pits_sold = 6
    pits_left = pits_sprouted - pits_sold
    result = pits_left
    return result

print(solution())