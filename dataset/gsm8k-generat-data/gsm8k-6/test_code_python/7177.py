def solution():
    # Calculate the total number of insects eaten
    geckos_insects = 5 * 6  # each gecko eats 6 insects
    lizards_insects = 3 * 2 * geckos_insects  # each lizard eats twice as much as a gecko
    total_insects = geckos_insects + lizards_insects
    result = total_insects
    return result

print(solution())