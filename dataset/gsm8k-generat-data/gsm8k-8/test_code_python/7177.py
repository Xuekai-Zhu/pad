def solution():
    # Calculate the total number of insects eaten by the geckos
    gecko_insects = 5 * 6

    # Calculate the total number of insects eaten by the lizards
    lizard_insects = 3 * 2 * gecko_insects

    # Calculate the total number of insects eaten
    total_insects = gecko_insects + lizard_insects
    result = total_insects
    return result

print(solution())