def solution():
    # Calculate the number of female cats and kittens
    female_cats = 6 / 2
    female_kittens = female_cats * 7

    # Calculate the remaining number of cats and kittens after selling 9 kittens
    remaining_cats = 6 + female_kittens - 9
    remaining_kittens = female_kittens - 9

    # Calculate the percentage of remaining cats that are kittens
    percent_kittens = round((remaining_kittens / remaining_cats) * 100)

    result = percent_kittens
    return result

print(solution())