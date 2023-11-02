def solution():
    # Calculate the number of female cats and kittens
    female_cats = 6 / 2
    kittens = female_cats * 7
    remaining_cats = 6 + kittens - 9  # subtract the 9 sold kittens from the total number of cats

    # Calculate the percentage of remaining cats that are kittens
    percentage_kittens = (kittens / remaining_cats) * 100
    result = round(percentage_kittens)
    return result

print(solution())