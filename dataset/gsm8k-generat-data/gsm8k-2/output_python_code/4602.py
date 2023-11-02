def solution():
    """Matt has six cats and half of them are female. If each female cat has 7 kittens, and Matt sells 9 of them, what percentage of his remaining cats are kittens (rounded to the nearest percent)?"""
    num_cats = 6
    num_female_cats = num_cats // 2
    num_kittens = num_female_cats * 7 - 9
    remaining_cats = num_cats - num_female_cats
    total_cats = remaining_cats + num_kittens
    kitten_percentage = (num_kittens / total_cats) * 100
    result = round(kitten_percentage)
    return result

print(solution())