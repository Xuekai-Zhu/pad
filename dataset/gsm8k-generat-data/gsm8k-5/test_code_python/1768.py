def solution():
    starting_cats = 20  # Jeff has 20 cats in his shelter
    new_kittens = 2  # Jeff found 2 new kittens on Monday
    injured_cat = 1  # Jeff found 1 injured cat on Tuesday
    adopted_cats = 3 * 2  # 3 people adopted 2 cats each on Wednesday

    # Calculate the total number of cats currently in Jeff's shelter
    total_cats = starting_cats + new_kittens + injured_cat - adopted_cats
    result = total_cats
    return result

print(solution())