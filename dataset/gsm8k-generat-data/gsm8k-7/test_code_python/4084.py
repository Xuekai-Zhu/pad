def solution():
    total_flowers = 12
    daisies = 2

    # calculate the number of remaining flowers after removing the daisies
    remaining_flowers = total_flowers - daisies

    # calculate the number of tulips
    tulips = remaining_flowers * (3/5)

    # calculate the number of sunflowers
    sunflowers = remaining_flowers - tulips

    result = sunflowers
    return result

print(solution())