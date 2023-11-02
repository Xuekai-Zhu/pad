def solution():
    crates_bought_1 = 6
    crates_bought_2 = 5
    crates_given = 2
    eggs_per_crate = 30
    total_eggs = (crates_bought_1 + crates_bought_2 - crates_given) * eggs_per_crate
    result = total_eggs
    return result

print(solution())