def solution():
    skins_per_coat = 15
    num_minks = 30
    babies_per_mink = 6

    # Calculate the total number of minks Andy has after their babies are born
    total_minks = num_minks + (num_minks * babies_per_mink)

    # Calculate the number of minks that were set free by activists
    free_minks = total_minks / 2

    # Calculate the number of mink skins Andy has left to make coats
    skins_left = (total_minks - free_minks) * skins_per_coat

    # Calculate the number of coats Andy can make
    num_coats = skins_left / skins_per_coat
    result = num_coats
    return result

print(solution())