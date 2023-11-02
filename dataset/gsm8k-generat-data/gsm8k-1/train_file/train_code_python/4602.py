def solution():
    """Matt has six cats and half of them are female. If each female cat has 7 kittens, and Matt sells 9 of them, what percentage of his remaining cats are kittens (rounded to the nearest percent)?"""
    num_cats = 6
    num_female_cats = num_cats / 2
    num_kittens = num_female_cats * 7
    num_kittens_remaining = num_kittens - 9
    num_cats_remaining = num_cats - 9
    percentage_kittens_remaining = round(num_kittens_remaining / num_cats_remaining * 100)
    result = percentage_kittens_remaining
    return result

print(solution())