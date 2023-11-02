def solution():
    cat1_blue_kittens = 3
    cat1_brown_kittens = 7

    cat2_blue_kittens = 4
    cat2_brown_kittens = 6

    # Calculate the total number of kittens with blue eyes
    total_blue_kittens = cat1_blue_kittens + cat2_blue_kittens

    # Calculate the total number of kittens
    total_kittens = cat1_blue_kittens + cat1_brown_kittens + cat2_blue_kittens + cat2_brown_kittens

    # Calculate the percentage of kittens with blue eyes
    percent_blue_kittens = (total_blue_kittens / total_kittens) * 100
    result = percent_blue_kittens
    return result

print(solution())