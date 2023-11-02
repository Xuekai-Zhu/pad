def solution():
    total_cats = 6  # Matt has six cats
    female_cats = total_cats / 2  # Half of Matt's cats are female
    female_kittens = female_cats * 7  # Each female cat has 7 kittens
    remaining_kittens = female_kittens - 9  # Matt sells 9 kittens

    # Calculate the total number of remaining cats
    remaining_cats = total_cats - (female_cats / 2) - (9 / 7)

    # Calculate the percentage of remaining cats that are kittens, rounded to the nearest percent
    kitten_percentage = round((remaining_kittens / remaining_cats) * 100)

    result = kitten_percentage
    return result

print(solution())