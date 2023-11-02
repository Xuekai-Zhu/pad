def solution():
    Hershels_fish = 10 + 15
    Bexleys_fish = 2/5 * 10 + 1/3 * 15
    Given_away = 1/2 * (10 + 15)
    Remaining_fish = Hershels_fish + Bexleys_fish - Given_away
    result = Remaining_fish
    return result

print(solution())