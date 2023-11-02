def solution():
    seeds_per_apple = 6
    seeds_per_pear = 2
    seeds_per_grape = 3

    apples_collected = 4
    pears_collected = 3
    grapes_collected = 9

    seeds_collected = (seeds_per_apple * apples_collected) + (seeds_per_pear * pears_collected) + (seeds_per_grape * grapes_collected)
    seeds_needed = 60 - seeds_collected

    result = seeds_needed
    return result

print(solution())