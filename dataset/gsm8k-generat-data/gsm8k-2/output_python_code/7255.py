def solution():
    """My 2 cats had 3 female kittens and 2 male kittens. How many cats do I have in total?"""
    cats = 2  # start with the 2 original cats
    female_kittens = 3
    male_kittens = 2
    total_kittens = female_kittens + male_kittens
    cats += total_kittens
    result = cats
    return result

print(solution())