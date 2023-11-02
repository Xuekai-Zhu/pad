def solution():
    num_cats = 6

    # Calculate the number of female cats
    num_female_cats = num_cats / 2

    # Calculate the number of kitten born
    num_kittens = num_female_cats * 7

    # Calculate the number of kittens remaining after selling 9
    num_kittens_remaining = num_kittens - 9

    # Calculate the total number of cats remaining
    num_cats_remaining = num_cats - (num_cats / 2) + (num_kittens_remaining / 7)

    # Calculate the percentage of remaining cats that are kittens
    percent_kittens = num_kittens_remaining / num_cats_remaining * 100
    result = round(percent_kittens)
    return result

print(solution())